from rest_framework import serializers
from .models import Shoes

class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes 
        fields = ('shoes_id', 'brand', 'name', 'color', 'price', 'price_before', 'image', 'slug')