from rest_framework.serializers import ModelSerializer

from .address import AddressSerializer
from .allergen import AllergenSerializer
from .api_user import APIUserSerializer
from .dietary_filter import DietaryFilterSerializer
from .image import ImageSerializer
from .ingredient import IngredientSerializer
from .price import PriceSerializer
from .uuid import UUIDModelSerializerMixin
from ..models import Meal


# FIXME: Merge these two serializers into one that can handle variants

class RetrieveMealSerializer(UUIDModelSerializerMixin, ModelSerializer):
    """A meal serializer used for List/Retrieve CRUD/REST operations"""
    allergens = AllergenSerializer(many=True)
    dietary_filters = DietaryFilterSerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    pickup_address = AddressSerializer()
    price = PriceSerializer()
    seller = APIUserSerializer()
    preview_image = ImageSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Meal
        fields = (
            'id',
            'name',
            'description',
            'allergens',
            'dietary_filters',
            'ingredients',
            'pickup_address',
            'portions',
            'portions_available',
            'price',
            'available_from',
            'available_to',
            'seller',
            'preview_image',
            'images'
        )
        depth = 1


class CreateUpdateMealSerializer(UUIDModelSerializerMixin, ModelSerializer):
    """A meal serializer used for Create/Update CRUD/REST operations"""

    class Meta:
        model = Meal
        fields = (
            'id',
            'name',
            'description',
            'allergens',
            'dietary_filters',
            'ingredients',
            'pickup_address',
            'portions',
            'portions_available',
            'price',
            'available_from',
            'available_to',
            'seller',
            'preview_image',
            'images'
        )
