import unittest
from app.models import Articles


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles()

    def test_articles(self):
        self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()
