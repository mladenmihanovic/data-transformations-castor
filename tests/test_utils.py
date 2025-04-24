import unittest
from src.utils import obfuscate_email_address

class TestUtils(unittest.TestCase):
    def test_obfuscate_email_address(self):
        email = "test@castor.com"
        obfuscated_email = obfuscate_email_address(email)

        self.assertEqual(obfuscated_email[4], "@")
        self.assertEqual(obfuscated_email[11], ".")
        self.assertEqual(len(obfuscated_email), len(email))
        self.assertNotEqual(obfuscated_email, email)

if __name__ == '__main__':
    unittest.main() 