from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from guardian.shortcuts import assign_perm
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from instameals.permissions import MealPermissions
from .base import NoDeleteModelViewSet
from ..models import Meal
from ..serializers import CreateUpdateMealSerializer, RetrieveMealSerializer


class MealViewSet(NoDeleteModelViewSet):
    """A REST Framework viewset for the Meal model."""
    queryset = Meal.objects.all()
    serializer_class = RetrieveMealSerializer
    permission_classes = (MealPermissions,)

    def create(self, request, *args, **kwargs):
        """"""
        # Serialize and validate the meal, setting seller to be the current user
        serializer = CreateUpdateMealSerializer(data=request.data)
        serializer.initial_data['seller'] = request.user.id
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Set permissions on the new meal
        assign_perm('change_meal', request.user, serializer.instance)
        assign_perm('delete_meal', request.user, serializer.instance)

        # Respond with created data
        headers = self.get_success_headers(serializer.data)
        response_serializer = self.serializer_class(serializer.instance,
                                                    context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """"""
        queryset = self.get_queryset()

        longitude = self.request.query_params.get('lng', None)
        latitude = self.request.query_params.get('lat', None)

        # FIXME: honor these query params
        # max_range = self.request.query_params.get('range', None)
        # units = self.request.query_params.get('units', 'mi')
        # limit = self.request.query_params.get('limit', None)
        # page = self.request.query_params.get('page', None)

        # FIXME: fail on bad input
        # Only obey latitude and longitude if we have both
        if all((latitude, longitude)):
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except ValueError:  # they weren't floats
                longitude, latitude = (-84.51, 39.10)
        else:
            longitude, latitude = (-84.51, 39.10)

        # FIXME: handle units and range
        # Convert max range to meters
        max_range = 15.0 * 1609.34

        query_location = Point(longitude, latitude)

        # Get meals within range and order them by distance from query_location
        meals = queryset.filter(
                is_active=True,
                pickup_address__coordinates__distance_lte=(
                    query_location, D(m=max_range)
                ),
        ).annotate(
                distance=Distance('pickup_address__coordinates', query_location)
        ).order_by('distance')

        serializer = self.serializer_class(meals, many=True, context={'request': request})

        # FIXME: paginate here
        return Response(serializer.data)
