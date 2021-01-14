from test_setup import TestSetUp

class TestViews(TestSetUp):
    
    def test_feedback_create_object_with_correct_data(self):
        res = self.client.post(self.register_new_feedback_url, self.feedback_data, format = "json")
        print()
        print('COMMENT: CREATE FEEDBACK OBJECT')
        print('SENT DATA: ', end='')
        print(self.feedback_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 201)
    
    def test_feedback_get_first_feedback_object(self):
        res = self.client.get(self.first_feedback_url)
        print()
        print('COMMENT: GET FIRST FEEDBACK DATA')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_feedback_update_second_feedback_object(self):
        res = self.client.put(self.second_feedback_url, self.feedback_data, format = "json")
        print()
        print('COMMENT: UPDATE SECOND FEEDBACK OBJECT DATA')
        print('SENT DATE: ', end='')
        print(self.feedback_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_feedback_delete_second_feedback_object(self):
        res = self.client.delete(self.second_feedback_url)
        print()
        print('COMMENT: DELETE SECOND FEEDBACK OBJECT DATA')
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 204)