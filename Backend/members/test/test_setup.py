from rest_framework.test import APITestCase
from members.models import Users

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = 'http://127.0.0.1:8000/api/user/'
        self.first_user_url = 'http://127.0.0.1:8000/api/user/1/'
        self.second_user_url = 'http://127.0.0.1:8000/api/user/2/'

        self.user_data = {
            "firstName": "test1",
            "lastName": "test2",
            "password": "password",
            "mobileNumber": "000011112222",
            "gender": "other",
            "email": "abdulla@acubed.com",
            "dateOfBirth": "25/3/1988",
            "type": "resident"
        }

        self.user_data_incorrect = {
            "firstName": "test1",
            "lastName": "test2",
            "password": "password",
            "mobileNumber": "000011112222",
            "gender": "other",
            "email": "noemail",
            "dateOfBirth": "25/3/1988",
            "type": "resident"
        }

        # self.user1 = {
        #     "firstName": "John",
        #     "lastName": "Alba",
        #     "password": "password123",
        #     "mobileNumber": "123456789",
        #     "gender": "male",
        #     "email": "john@gmail.com",
        #     "dateOfBirth": "5/12/1960",
        #     "type": "admin"
        # }

        # self.user2 = {
        #     "firstName": "Sypha",
        #     "lastName": "Belmont",
        #     "password": "password123",
        #     "mobileNumber": "123456789",
        #     "gender": "female",
        #     "email": "sypha@gmail.com",
        #     "dateOfBirth": "4/16/1925",
        #     "type": "staff"
        # }

        Users.objects.create(firstName="John", lastName="Alba", password="password123", mobileNumber="123456789", gender="male", email="john@gmail.com", dateOfBirth="5/12/1960", type="admin")
        Users.objects.create(firstName="Sypha", lastName="Belmont", password="password123", mobileNumber="123456789", gender="female", email="sypha@gmail.com", dateOfBirth="4/16/1925", type="staff")

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
