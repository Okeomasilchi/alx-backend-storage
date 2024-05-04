import unittest
from exercise import Cache

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache()

    def test_get_int_existing_key(self):
        key = "my_key"
        value = 42
        self.cache.store(value)
        result = self.cache.get_int(key)
        self.assertEqual(result, value)

    def test_get_int_non_existing_key(self):
        key = "non_existing_key"
        result = self.cache.get_int(key)
        self.assertIsNone(result)

    def test_get_int_non_convertible_value(self):
        key = "my_key"
        value = "not_an_int"
        self.cache.store(value)
        result = self.cache.get_int(key)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()