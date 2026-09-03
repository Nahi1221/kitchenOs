from rest_framework import serializers
from .models import MenuCategory, MenuItem, Modifier

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'price', 'currency',
            'image_url', 'is_available', 'is_active', 'is_out_of_stock',
            'featured', 'order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = [
            'id', 'name', 'description', 'is_active', 'order', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = [
            'id', 'item', 'name', 'price_adjustment', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
