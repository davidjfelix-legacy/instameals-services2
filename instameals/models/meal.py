import uuid

from django.db import models

from .allergen import Allergen
from .api_user import APIUser
from .dietary_filter import DietaryFilter
from .ingredient import Ingredient
from .location import Location


class Meal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=10000)
    allergens = models.ManyToManyField(Allergen, blank=True)
    dietary_filters = models.ManyToManyField(DietaryFilter, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    # FIXME: validate positive
    portions = models.IntegerField()
    portions_available = models.IntegerField()

    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    # FIXME: validate dates
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE)

    class Meta:
        app_label = 'instameals'
