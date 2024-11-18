import unittest
from main import hello_group_51_52_lms

class TestMain(unittest.TestCase):
    def test_hello_group_51_52_lms(self):
        student_output = hello_group_51_52_lms()
        expected_output = "Hello Group-51-52 lms"
        
        self.assertEqual(student_output, expected_output)


if __name__ == "__main__":
    unittest.main()