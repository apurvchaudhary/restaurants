from rest_framework.views import APIView
from . import utils


class UploadData(APIView):
    """
    API to upload data with script
    """
    def get(self, request):
        return utils.upload_restaurant()


class UploadLocations(APIView):
    """
    API to upload location data with script
    """
    def get(self, request):
        return utils.upload_restaurant_locations()


class GetAllRestaurant(APIView):
    """
    API to get list of all restaurant
    """
    def get(self, request):
        return utils.get_all_restaurant(request)


class GetRestaurantByPrice(APIView):
    """
    API to get restaurant by price
    """
    def get(self, request):
        price = int(request.query_params.get('price'))
        return utils.get_restaurant_by_price(request, price=price)


class GetRestaurantByVotes(APIView):
    """
    API to get restaurant by price
    """
    def get(self, request):
        vote = int(request.query_params.get('votes'))
        return utils.get_restaurant_by_votes(request, vote=vote)


class GetRestaurantByCuisine(APIView):
    """
    API to get restaurant by cuisine
    """
    def get(self, request):
        cuisine = request.query_params.get('cuisine')
        return utils.get_restaurant_by_cuisine(request, cuisine=cuisine)

    def post(self, request):
        cuisine = dict(request.data)['cuisine']
        return utils.get_restaurant_by_cuisine(request, cuisine=cuisine)


class GetRestaurantByName(APIView):
    """
    API to get restaurant by name
    """
    def get(self, request):
        restaurant_name = request.query_params.get('name')
        return utils.get_restaurant_by_name(request, name=restaurant_name)