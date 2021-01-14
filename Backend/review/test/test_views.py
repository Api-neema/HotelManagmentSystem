from test_setup import TestSetUp


class TestViews(TestSetUp):
    
    def test_review_create_object_with_correct_data(self):
        res = self.client.post(self.register_new_review_url, self.review_data, format = "json")
        print()
        print('COMMENT: CREATE REVIEW OBJECT')
        print('SENT DATA: ', end='')
        print(self.review_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 201)
    
    def test_review_get_first_booking_object(self):
        res = self.client.get(self.first_review_url)
        print()
        print('COMMENT: GET FIRST REVIEW DATA')
        print(res.data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_review_update_second_review_object(self):
        res = self.client.put(self.second_review_url, self.review_data, format = "json")
        print()
        print('COMMENT: UPDATE SECOND REVIEW OBJECT DATA')
        print('SENT DATE: ', end='')
        print(self.review_data)
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 200)

    def test_review_delete_second_booking_object(self):
        res = self.client.delete(self.second_review_url)
        print()
        print('COMMENT: DELETE SECOND REVIEW OBJECT DATA')
        print('STATUS CODE: ' + str(res.status_code) + '\r\n')
        self.assertEqual(res.status_code, 204)