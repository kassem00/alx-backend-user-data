import unittest
from unittest.mock import MagicMock
from api.v1.auth.auth import Auth  # Assuming this is where your Auth class is located

class TestAuth(unittest.TestCase):
    
    def setUp(self):
        """Initialize the Auth object before each test"""
        self.auth = Auth()

    def test_authorization_header_no_request(self):
        """Test when request is None"""
        self.assertIsNone(self.auth.authorization_header(None))

    def test_authorization_header_with_authorization(self):
        """Test when Authorization header is present"""
        mock_request = MagicMock()
        mock_request.headers = {'Authorization': 'Bearer test_token'}

        self.assertEqual(self.auth.authorization_header(mock_request), 'Bearer test_token')

    def test_authorization_header_no_authorization(self):
        """Test when Authorization header is not present"""
        mock_request = MagicMock()
        mock_request.headers = {}

        self.assertIsNone(self.auth.authorization_header(mock_request))

if __name__ == '__main__':
    unittest.main()
