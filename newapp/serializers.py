from rest_framework.serializers import ModelSerializer

from .models import Shop,Street,City


class ShopSerializers(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name','house_number','openTime','closeTime']

class StreetSerializers(ModelSerializer):
    class Meta:
        model = Street
        fields = ['street_name','shops']

class CitySerializers(ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name','streets']