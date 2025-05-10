''' tests flask app
file: test_app.py   
'''
import unittest
import app as a

class TestApp(unittest.TestCase):
    '''class for tests for app.py'''

    def setUp(self):
        '''set up for testing'''
        self.app = a.app.test_client()

    def test_homepage(self):
        '''test homepage returns the correct message'''
        response = self.app.get('/')
        self.assertEqual(b"Hello, this is the homepage for the leisure time data. " \
            b"To see the most common activitiy that people spend their time on for a certain age" \
            b" add a '/' to this URL followed by the age you would like to look at " \
            b"(age options: 18, 23, 40, 56, 57, 71, 80).", response.data)

    def test_get_top_activity(self):
        '''test get_top_activity returns the correct top activity for the given age'''
        response = self.app.get('/23')
        self.assertEqual(b"Financial management", response.data)

    def test_get_top_activity_invalid_age(self):
        '''test get_top_activity returns the correct error message for invalid age'''
        response = self.app.get('/100')
        self.assertEqual(b"500 Internal Server Error: The server encountered an internal error " \
            b"and was unable to complete your request. Either the server is overloaded or there " \
            b"is an error in the application. Invalid age, choose a valid age based on the small" \
            b" dataset: 18, 23, 40, 56, 57, 71, 80", response.data)

    def test_404_error(self):
        '''test 404 error returns the correct error message'''
        response = self.app.get('/invalid')
        self.assertIn(b"404 Not Found: The requested URL was not found on the server.", 
                      response.data)
