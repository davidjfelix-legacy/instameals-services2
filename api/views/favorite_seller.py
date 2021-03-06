from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import FavoriteSeller
from ..serializers import FavoriteSellerSerializer


# FIXME: change viewset to allow deletions
class FavoriteSellerViewSet(NoDeleteModelViewSet):
    queryset = FavoriteSeller.objects.all()
    serializer_class = FavoriteSellerSerializer
    # FIXME: a user should be able to see their favorites or favorites of them only
    # FIXME: Use this: permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)


class MyFavoriteSellerViewSet(FavoriteSellerViewSet):
    def get_queryset(self):
        return FavoriteSeller.objects.filter(favoriter=self.request.user)


class MyFollowerViewSet(FavoriteSellerViewSet):
    def get_queryset(self):
        return FavoriteSeller.objects.filter(seller=self.request.user)
