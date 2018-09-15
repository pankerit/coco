from rest_framework import serializers
from .models import Shoes



class ShoesSerializer(serializers.ModelSerializer):
    # sizes = Shoes_sizeSerializer(many=True)
    class Meta:
        model = Shoes 
        # fields = ('shoes_id', 'brand', 'name', 'color', 'price', 'price_before', 'image', 'slug', 'sizes')
        fields = ('shoes_id', 'brand', 'name', 'color', 'price', 'price_before', 'image', 'slug', 'sizes', 'images', 'images_3d')


