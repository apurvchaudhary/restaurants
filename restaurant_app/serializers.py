from rest_framework import serializers
from . import models

class GetRestaurantSerializer(serializers.ModelSerializer):
    """
    serializing restaurant object
    """
    location = serializers.SerializerMethodField()
    cuisine = serializers.SerializerMethodField()
    class Meta:
        model = models.Restaurant
        fields = '__all__'

    def get_cuisine(self, obj):
        return [c.cuisine_name for c in obj.restaurant_cuisine.all()]
    def get_location(self, obj):
        return obj.restaurant_location.values('latitude' , 'longitude', 'address')
