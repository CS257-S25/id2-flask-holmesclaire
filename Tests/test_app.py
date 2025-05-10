''' tests flask app
    - test_app.py   
'''
import unittest
import app as app


class TestApp(unittest.TestCase):
    '''class for tests for app.py'''

    def test_homepage(self):
        '''test homepage returns the correct message'''
        response = app.get('/')
        self.assertEqual("Hello, this is the homepage for the leisure time data. " \
            "To see the most common activitiy that people spend their time on for a certain age" \
            " add a '/' to this URL followed by the age you would like to look at " \
            "(age options: 18, 23, 40, 56, 57, 71, 80).", response.data)
        
    def test_get_top_activity(self):
        '''test get_top_activity returns the correct top activity for the given age'''
        response = app.get('/23')
        self.assertEqual("Financial management", response.data)

    def test_get_top_activity_invalid_age(self):
        '''test get_top_activity returns the correct error message for invalid age'''
        response = app.get('/100')
        self.assertEqual("Invalid age, choose a valid age based on the small dataset: 18, 23, 40, 56, 57, 71, 80", response.data)
