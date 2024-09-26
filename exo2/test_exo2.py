import unittest
from exo2 import solution  # Import the solution function from solution.py

class TestSolution(unittest.TestCase):
    
    def test_fixed_tests_True(self):
        fixed_tests_True = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        ]
        for string, ending in fixed_tests_True:
            with self.subTest(string=string, ending=ending):
                self.assertTrue(solution(string, ending))
    
    def test_fixed_tests_False(self):
        fixed_tests_False = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        ]
        for string, ending in fixed_tests_False:
            with self.subTest(string=string, ending=ending):
                self.assertFalse(solution(string, ending))

# Running the tests
if __name__ == "__main__":
    unittest.main()
