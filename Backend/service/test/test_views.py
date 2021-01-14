from test_setup import TestSetUp

class TestViews(TestSetUp):

    def test_service_cannot_register_with_incorrect_data(self):
        res = self.client.post(self.register_new_service_url, self.service_data_incorrect, format = "json")
        print()
        print('COMMENT: SERVICE CANNOT BE REGISTERD AS `fees` IS MISSING')
        print('SENT DATA: ', end='')
        print(self.service_data_incorrect)
        print('FAILURE MESSAGE: ', end='')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 400)  
    
    def test_service_create_object_with_correct_data(self):
        res = self.client.post(self.register_new_service_url, self.service_data, format = "json")
        print()
        print('COMMENT: CREATE SERVICE OBJECT')
        print('SENT DATA: ', end='')
        print(self.service_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 201)
    
    def test_service_get_first_service_object(self):
        res = self.client.get(self.first_service_url)
        print()
        print('COMMENT: GET FIRST SERVICE DATA')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_service_update_second_service_object(self):
        res = self.client.put(self.second_service_url, self.service_data, format = "json")
        print()
        print('COMMENT: UPDATE SECOND SERVICE OBJECT DATA')
        print('SENT DATE: ', end='')
        print(self.service_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_service_delete_second_service_object(self):
        res = self.client.delete(self.second_service_url)
        print()
        print('COMMENT: DELETE SECOND SERVICE OBJECT DATA')
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 204)