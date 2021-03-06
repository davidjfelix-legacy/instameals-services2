from django.conf import settings
from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .address import Address
from .meal import Meal
from .price import Price
from .uuid import UUIDModelMixin


class Order(UUIDModelMixin, TimeStampedModel):
    buyer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='buyer_orders'
    )
    purchased_at = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Meal)
    buyer_price = models.OneToOneField(Price, related_name='buyer_order')
    seller_earnings = models.OneToOneField(Price, related_name='seller_order')
    billing_address = models.ForeignKey(
            Address,
            on_delete=models.CASCADE,
            related_name='billed_orders',
    )
    pickup_address = models.ForeignKey(
            Address,
            on_delete=models.CASCADE,
            related_name='pickup_orders',
    )
    pickup_time = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        app_label = 'api'
        permissions = (
            ('view_order', 'Can view order'),
        )

    def __str__(self):
        return "[{id}]: {buyer}'s purchase of {meal} at {purchased_at}".format(
                id=str(self.id),
                buyer=str(self.buyer),
                meal=str(self.meal),
                purchased_at=str(self.purchased_at),
        )
