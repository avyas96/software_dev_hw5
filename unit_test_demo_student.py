import unittest
from student import Student

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        john = Student("John", 1, 111222333, "212 West Ave", 20, "Computer Science")
        self.assertEqual(john.getName(), "John")
        self.assertEqual(john.getId(), 1)
        self.assertEqual(john.getAge(),16)


if __name__ == '__main__':
    unittest.main()