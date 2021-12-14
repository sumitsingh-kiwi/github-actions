"""
project/test_basic.py
"""
import unittest

from app import app


class BasicTests(unittest.TestCase):
    """
    setup and teardown
    """

    # executed prior to each test
    def setUp(self):
        """ setup function """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        """ tear down function"""
        pass

    # tests
    def test_main_page(self):
        """ main page test case """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    """ call the main file """
    unittest.main()
