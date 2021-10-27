from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Shop,Street,City
from .serializers import ShopSerializers,StreetSerializers,CitySerializers


def index(request) :
    return render(request, 'main/index.html')

def view_page(request):
    return render(request, 'index.html',{'shop': Shop.objects.all()})

class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class StreetView(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializers

class ShopView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


