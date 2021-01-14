from rest_framework.test import APITestCase
from review.models import review

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_new_review_url = 'http://127.0.0.1:8000/api/reviews/'
        self.first_review_url = 'http://127.0.0.1:8000/api/reviews/1/'
        self.second_review_url = 'http://127.0.0.1:8000/api/reviews/2/'

        self.review_data = {
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "rating": "1",
            "userName": "user1"
        }

        review.objects.create(description="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", rating="5", userName="user3")
        review.objects.create(description="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", rating="4.5", userName="user4")
        

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
