import pandas as pd
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import serializers


def response(data, code=status.HTTP_200_OK):
    """
    Overrides rest_framework response
    :param data: data to be send in response
    :param code: response status code(default has been set to 200)
    :param error: error message(if any, not compulsory)
    """
    return Response(data=data, status=code)


def get_all_restaurant(request):
    """
    utility to return list of all restaurant
    :return: restaurants
    """
    restaurants = models.Restaurant.objects.prefetch_related('restaurant_cuisine', 'restaurant_location')
    serializer = serializers.GetRestaurantSerializer(restaurants, many=True)
    return render(request=request, template_name='home.html', context={'data' : serializer.data})


def get_restaurant_by_price(request, price):
    if price == 1000:
        restaurants = models.Restaurant.objects.filter(cost_for_two__lte=1000).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    elif price == 2000:
        restaurants = models.Restaurant.objects.filter(cost_for_two__lte=2000).exclude(cost_for_two__lte=1000).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    elif price == 3000:
        restaurants = models.Restaurant.objects.filter(cost_for_two__gt=2000).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    serializer = serializers.GetRestaurantSerializer(restaurants, many=True)
    return render(request=request, template_name='home.html', context={'data': serializer.data})


def get_restaurant_by_votes(request, vote):
    if vote == 100:
        restaurants = models.Restaurant.objects.filter(votes__lte=100).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    elif vote == 200:
        restaurants = models.Restaurant.objects.filter(votes__lte=500).exclude(votes__lte=100).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    elif vote == 500:
        restaurants = models.Restaurant.objects.filter(votes__gt=500).\
            prefetch_related('restaurant_cuisine', 'restaurant_location')
    serializer = serializers.GetRestaurantSerializer(restaurants, many=True)
    return render(request=request, template_name='home.html', context={'data': serializer.data})


def get_restaurant_by_cuisine(request, cuisine):
    queryset = models.Cuisine.objects.filter(cuisine_name__in=cuisine).\
        prefetch_related('restaurant_field')
    restaurants = [i.restaurant_field for i in queryset]
    serializer = serializers.GetRestaurantSerializer(restaurants, many=True)
    return render(request=request, template_name='home.html', context={'data': serializer.data})


def get_restaurant_by_name(request, name):
    if not name:
        return render(request=request, template_name='home.html', context={'error': 'No result for empty restaurant name...!'})
    restaurants = models.Restaurant.objects.filter(name__contains=name).\
        prefetch_related('restaurant_cuisine', 'restaurant_location')
    if not restaurants:
        return render(request=request, template_name='home.html', context={'error': 'We did not find any restaurant with this name...!'})
    serializer = serializers.GetRestaurantSerializer(restaurants, many=True)
    return render(request=request, template_name='home.html', context={'data': serializer.data})


def upload_restaurant():
    """
    utility to upload sheet data to restaurant table
    """
    df = pd.read_csv('/Users/apurvchaudhary/Desktop/restaurant_folder/restaurant/restaurantsa9126b3.csv')
    restaurant_id = df['Restaurant ID']
    name = df['Restaurant Name']
    cost_for_two = df['Average Cost for two']
    currency = df['Currency']
    table_booking_ = df['Has Table booking']
    online_delivery_ = df['Has Online delivery']
    rating = df['Aggregate rating']
    rating_color = df['Rating color']
    rating_text = df['Rating text']
    votes = df['Votes']
    for i in range(len(df)):
        if table_booking_[i] == 'Yes':
            table_booking = True
        else:
            table_booking = False
        if online_delivery_[i] == 'Yes':
            online_delivery = True
        else:
            online_delivery = False
        try:
            restaurant = models.Restaurant.objects.create(restaurant_id=restaurant_id[i], name=name[i], cost_for_two=cost_for_two[i],
                                               currency=currency[i], table_booking=table_booking, online_delivery=online_delivery,
                                               rating=rating[i], rating_color=rating_color[i], rating_text=rating_text[i], votes=votes[i])
            restaurant.save()
            for i in df['Cuisines'][i].split(','):
                cuisine = models.Cuisine.objects.create(restaurant_field=restaurant, cuisine_name=i)
                cuisine.save()
        except Exception as e:
            print('exception occured while creating restaurant object : ' + str(e))
    return response(data='Data uploaded Successfully')

def upload_restaurant_locations():
    """
    utility to upload sheet data to restaurant address table
    """
    df = pd.read_csv('/Users/apurvchaudhary/Desktop/restaurant_folder/restaurant/restaurant_addc9a1430.csv')
    restaurant_id = df['Restaurant ID']
    country_code = df['Country Code']
    city = df['City']
    address = df['Address']
    locality = df['Locality']
    locality_verbose = df['Locality Verbose']
    latitude = df['Latitude']
    longitude = df['Longitude']
    for i in range(len(df)):
        try:
            restaurant = models.Restaurant.objects.get(restaurant_id=restaurant_id[i])
        except ObjectDoesNotExist:
            print(f'object does not exist : {restaurant_id[i]}')
        else:
            location = models.Location.objects.create(restaurant_field=restaurant, c_code=country_code[i], city=city[i],
                                                     address=address[i], locality=locality[i], locality_verbose=locality_verbose[i],
                                                     latitude=latitude[i], longitude=longitude[i])
            location.save()
    return response(data='Locations uploaded Successfully')