import json
import decimal

from django.http      import JsonResponse
from django.views     import View

from review.models import Review
from hotel.models import Hotel
from user.models import User

# Create your views here.

class HotelReviewView(View):

    def get(self, request, hotel_id):
        hotel_id = hotel_id
        review_list = [review for review in Review.objects.filter(hotel_id = hotel_id).values()]

        returning_list = [
            {
                'hotel' : review['hotel_id'],
                'user' : review['user_id'],
                'rating' : review['rating'],
                'created_at' : review['created_at'].strftime("%Y-%m-%dT%H:%M:%S"),
                'title' : review['title'],
                'content' : review['content']
            }
            for review in review_list
        ]


        return JsonResponse(
            {'review_list':returning_list},
            status=200
        )