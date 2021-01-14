from rest_framework.test import APITestCase
from service.models import service

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_new_service_url = 'http://127.0.0.1:8000/api/services/'
        self.first_service_url = 'http://127.0.0.1:8000/api/services/1/'
        self.second_service_url = 'http://127.0.0.1:8000/api/services/2/'

        self.service_data = {
            "serviceName": "service 1",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "fees": "90$",
            "type": "type 1",
            "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2F",
        }

        self.service_data_incorrect = {
            "serviceName": "service 1",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "type": "type 2",
            "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2F",
        }


        service.objects.create(serviceName="service 1", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", fees="100$", type="type 1", image="https://www.google.com/url?sa=i&url=https%3A%2F%2F")
        service.objects.create(serviceName="service 2", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", fees="55$", type="type 2", image="https://www.google.com/url?sa=i&url=https%3A%2F%2F")
        

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
