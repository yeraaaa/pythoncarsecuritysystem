import unittest
from src.validation_module import validate_license

class TestValidationModule(unittest.TestCase):
    def test_validate_license(self):
        result = validate_license()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
