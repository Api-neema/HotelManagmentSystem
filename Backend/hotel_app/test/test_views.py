from test_setup import TestSetUp

class TestViews(TestSetUp):

    def test_hotel_cannot_register_with_incorrect_data(self):
        res = self.client.post(self.register_new_hotel_url, self.hotel_data_incorrect, format = "json")
        print()
        print('COMMENT: HOTEL CANNOT BE REGISTERD AS `hotelAddress` IS MISSING')
        print('SENT DATA: ', end='')
        print(self.hotel_data_incorrect)
        print('FAILURE MESSAGE: ', end='')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 400)  
    
    def test_hotel_create_object_with_correct_data(self):
        res = self.client.post(self.register_new_hotel_url, self.hotel_data, format = "json")
        print()
        print('COMMENT: CREATE HOTEL OBJECT')
        print('SENT DATA: ', end='')
        print(self.hotel_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 201)
    
    def test_hotel_get_first_hotel_object(self):
        res = self.client.get(self.first_hotel_url)
        print()
        print('COMMENT: GET FIRST HOTEL DATA')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_hotel_update_second_hotel_object(self):
        res = self.client.put(self.second_hotel_url, self.hotel_data, format = "json")
        print()
        print('COMMENT: UPDATE SECOND HOTEL OBJECT DATA')
        print('SENT DATE: ', end='')
        print(self.hotel_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_hotel_delete_second_hotel_object(self):
        res = self.client.delete(self.second_hotel_url)
        print()
        print('COMMENT: DELETE SECOND HOTEL OBJECT DATA')
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 204)