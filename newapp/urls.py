from rest_framework.routers import SimpleRouter
from .views import CityView,ShopView,StreetView

router = SimpleRouter()

router.register('api/city', CityView)
router.register('api/shop', ShopView)
router.register('api/street', StreetView)

urlpatterns = [
]

urlpatterns += router.urls