
import unittest

from app.models import News


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_source = News('bbc', 'image', 'testing image', 'monica')

    def test_sources(self):
        self.assertTrue(isinstance(self.new_source, News))


if __name__ == '__main__':
    unittest.main()