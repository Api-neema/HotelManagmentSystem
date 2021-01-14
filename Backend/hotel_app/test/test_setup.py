from rest_framework.test import APITestCase
from hotel_app.models import hotel

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_new_hotel_url = 'http://127.0.0.1:8000/api/hotel/'
        self.first_hotel_url = 'http://127.0.0.1:8000/api/hotel/1/'
        self.second_hotel_url = 'http://127.0.0.1:8000/api/hotel/2/'

        self.hotel_data = {
            "hotelName": "hotel 1",
            "hotelAddress": "Lorem Ipsum street",
            "singleRooms": "55",
            "doubleRooms": "40",
            "tripleRooms": "20",
        }

        self.hotel_data_incorrect = {
            "hotelName": "hotel 1",
            "singleRooms": "60",
            "doubleRooms": "60",
            "tripleRooms": "30",
        }


        hotel.objects.create(hotelName="hotel 3", hotelAddress="Lorem Ipsum street 2", singleRooms="100", doubleRooms="100", tripleRooms="100")
        hotel.objects.create(hotelName="hotel 4", hotelAddress="Lorem Ipsum street 3", singleRooms="200", doubleRooms="200", tripleRooms="200")
        

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
