from rest_framework import serializers
from .models import Shoes, Shoes_size

class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes 
        fields = ('shoes_id', 'brand', 'name', 'color', 'price', 'price_before', 'image', 'slug')
    
class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes 
        fields = ('shoes_id', 'brand', 'name', 'color', 'price', 'price_before', 'image', 'slug')