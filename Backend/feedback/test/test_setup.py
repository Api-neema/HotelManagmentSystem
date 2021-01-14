from rest_framework.test import APITestCase
from feedback.models import feedback

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_new_feedback_url = 'http://127.0.0.1:8000/api/feedback/'
        self.first_feedback_url = 'http://127.0.0.1:8000/api/feedback/1/'
        self.second_feedback_url = 'http://127.0.0.1:8000/api/feedback/2/'

        self.feedback_data = {
            "feedback": "feedback 1",
            "email": "ramadan@test.com",
            "userName": "AbdohRamadan"
        }

        feedback.objects.create(feedback="feedback 2", email="ramadan@test.net", userName="ThisIsAUserName")
        feedback.objects.create(feedback="feedback 3", email="Abdullah@test.net", userName="ThisIsAUserName2")
        

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
