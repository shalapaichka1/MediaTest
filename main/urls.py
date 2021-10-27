from django.urls import path
from rest_framework.routers import SimpleRouter


from . import views
## тебе тут не надо модель импортировать, тебе надо вьюшку-контроллер
from .views import ShopView,StreetView,CityView

router = SimpleRouter()

## и тут ты нахера модель Shop закидываешь если надо контроллер
router.register('api/city', CityView)
router.register('api/shop', ShopView)
router.register('api/street', StreetView)


urlpatterns = [
path('', views.index)
]

urlpatterns += router.urls