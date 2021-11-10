from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shop,Street,City
from .serializers import ShopSerializers,CitySerializers,StreetSerializers



def view_page(request):
    return render(request, '',{'shop': Shop.objects.all()})

class ShopView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers

class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class StreetView(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializers

