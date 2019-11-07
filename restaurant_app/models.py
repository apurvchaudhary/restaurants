from django.db import models

# Create your models here.
class ModelBase(models.Model):
    """
    Model to save created at and updated at time and date
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Restaurant(ModelBase):
    """
    Model to save restaurant details
    """
    restaurant_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    cost_for_two = models.IntegerField()
    currency = models.CharField(max_length=200)
    table_booking = models.BooleanField(default=False)
    online_delivery = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    rating_color = models.CharField(max_length=100)
    rating_text = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return f"restaurant id : {self.restaurant_id} and name : {self.name}"


class Cuisine(ModelBase):
    """
    Model to save restaurant's cuisines
    """
    restaurant_field = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_cuisine')
    cuisine_name = models.CharField(max_length=200)

    def __str__(self):
        return f"restaurant id : {self.restaurant_field} and cuisine : {self.cuisine_name}"

class Location(ModelBase):
    """
    Model to save restaurant location details
    """
    restaurant_field = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_location')
    c_code = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    locality = models.CharField(max_length=500)
    locality_verbose = models.CharField(max_length=600)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return f"restaurant id : {self.restaurant_field} and city : {self.city}"