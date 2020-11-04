from django.urls import path
from hotel.views import HotelListView

urlpatterns = [
    path('/hotels', HotelListView.as_view())
]
