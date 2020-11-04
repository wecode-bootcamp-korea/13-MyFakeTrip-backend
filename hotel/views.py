import json

from django.http import JsonResponse
from django.views import View

from hotel.models import Region, City, Hotel, Option, HotelOption, HotelImage, Convenience, HotelConvenience, Theme, HotelTheme
# Create your views here.

class HotelListView(View):
    # def get(self, request):
    #     region_id = request.GET.get('region', None)
    #     city_id = request.GET.get('city', None)

    #     if city_id:
    #         filter_condition = {'city_id': city_id}
    #     elif region_id:
    #         cities = City.objects.filter(region_id = region_id)
    #         filter_condition = {'cities' : cities}
    #     else:
    #         filter_condition = {'city_id': 1}

        
    #     hotel_list = Hotel.objects.filter(**filter_condition).values()

    #     data = [hotel for hotel in hotel_list]

    def get(self, request):
        category_id = request.GET.get('category', None)
        subcategory = request.GET.get('location', None)

        if category_id == 2:
            if location:
                filter_condition = {'location': city_id}
            else:
                filter_condition = {'location': 1}
        elif category_id == 1:
            if location:
                cities = City.objecst.filter(region_id = region_id)
                filter_condition = {'location': cities}
            else:
                filter_condition = {'location': 1}
        else:
            filter_condition = {'location': 1}

        
        hotel_list = Hotel.objects.filter(**filter_condition).values()
        data = [hotel for hotel in hotel_list]
    
                

        return JsonResponse(
            {
                "hotels":data
            },
            status=200
        )



        