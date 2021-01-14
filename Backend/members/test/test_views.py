from test_setup import TestSetUp
from members.models import Users

class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url, self.user_data_incorrect, format = "json")
        print()
        print('COMMENT: USER CANNOT REGISTER AS WRONG EMAIL IS IN USE')
        print('SENT DATA: ', end='')
        print(self.user_data_incorrect)
        print('FAILURE MESSAGE: ', end='')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 400)  
    
    def test_user_can_register_with_correct_data(self):
        res = self.client.post(self.register_url, self.user_data, format = "json")
        print()
        print('COMMENT: USER CAN REGISTER WITH CORRECT USER DATA')
        print('SENT DATA: ', end='')
        print(self.user_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 201)
    
    def test_user_get_first_user(self):
        res = self.client.get(self.first_user_url)
        print()
        print('COMMENT: GET FIRST USER DATA')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_user_update_second_user(self):
        res = self.client.put(self.second_user_url, self.user_data, format = "json")
        print()
        print('COMMENT: UPDATE SECOND USER DATA')
        print('SENT DATE: ', end='')
        print(self.user_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_user_delete_second_user(self):
        res = self.client.delete(self.second_user_url)
        print()
        print('COMMENT: DELETE SECOND USER DATA')
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 204)