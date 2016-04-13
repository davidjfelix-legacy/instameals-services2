from rest_framework.serializers import ModelSerializer

from .address import AddressSerializer
from .api_user import APIUserSerializer
from .meal import RetrieveMealSerializer
from .price import PriceSerializer
from .uuid import UUIDModelSerializerMixin
from ..models import Order


class OrderSerializer(UUIDModelSerializerMixin, ModelSerializer):
    buyer = APIUserSerializer()
    meal = RetrieveMealSerializer()
    buyer_price = PriceSerializer()
    seller_earnings = PriceSerializer()
    billing_address = AddressSerializer()
    pickup_address = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'buyer',
            'purchased_at',
            'meal',
            'buyer_price',
            'seller_earnings',
            'billing_address',
            'pickup_address',
        )
