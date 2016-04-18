from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import DietaryFilter
from ..serializers import DietaryFilterSerializer


# FIXME: use a writable viewset when permission_classes allows admin only writes
class DietaryFilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DietaryFilter.objects.all()
    serializer_class = DietaryFilterSerializer
    # FIXME: only allow admin to write
    permission_classes = (AllowAny,)
