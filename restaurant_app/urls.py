from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'uploaddata/', views.UploadData.as_view()),
    url(r'uploadlocations/', views.UploadLocations.as_view()),
    url(r'getallrestaurants/', views.GetAllRestaurant.as_view()),
    url(r'getrestaurantbyprice/', views.GetRestaurantByPrice.as_view()),
    url(r'getrestaurantbyvotes/', views.GetRestaurantByVotes.as_view()),
    url(r'getrestaurantbycuisine/', views.GetRestaurantByCuisine.as_view(), name='get_restaurant_by_cuisine'),
    url(r'getrestaurantbyname/', views.GetRestaurantByName.as_view(), name='get_restaurant_by_name')
]