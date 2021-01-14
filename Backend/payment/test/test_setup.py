from rest_framework.test import APITestCase
from payment.models import Payment

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_new_card_url = 'http://127.0.0.1:8000/api/card/'
        self.first_card_url = 'http://127.0.0.1:8000/api/card/1/'
        self.second_card_url = 'http://127.0.0.1:8000/api/card/2/'

        self.card_data = {
            "cardType": "card 2",
            "cardNumber": "000000000000",
            "expiryDate": "5/05",
        }
        
        self.card_data_incorrect = {
            "cardType": "card 3",
            "expiryDate": "5/07",
        }



        Payment.objects.create(cardType="card 4", cardNumber="000000001111", expiryDate="1/07")
        Payment.objects.create(cardType="card 5", cardNumber="000011112222", expiryDate="1/05")
        

        return super().setUp()
    
    
    def tearDown(self):
        return super().tearDown()
