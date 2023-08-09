import unittest

from TreeHouse.TreeCounter import TreeCounter


class TreeCounterTests(unittest.TestCase):
    def test_edge_trees_should_be_counted(self):
        tests = [
            ([[1, 2, 3], [4, 1, 5], [6, 7, 8]], 8),
            ([[0, 0, 0, 0, 0]] * 5, 16)
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(TreeCounter().count(value), expected)

    def test_small_forest_with_no_cover(self):
        tests = [
            ([[1, 2], [3, 4]], 4),
            ([[1, 2, 3], [4, 9, 5], [6, 7, 8]], 9),
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(TreeCounter().count(value), expected)

    def test_given_case(self):
        value= [[3, 0, 3, 7, 3],
         [2, 5, 5, 1, 2],
         [6, 5, 3, 3, 2],
         [3, 3, 5, 4, 9],
         [3, 5, 3, 9, 0]]
        self.assertEqual(TreeCounter().count(value), 21)

    def test_amazon(self):
        with open('big_test.txt', 'r') as file:
            lines = file.readlines()
        forest = []
        for line in lines:
            row = [int(digit) for digit in line.strip()]
            forest.append(row)
        self.assertEqual(TreeCounter().count(forest), 1679)

    def test_highest_scenic_score_of_forest(self):
        value = [[3, 0, 3, 7, 3],
                 [2, 5, 5, 1, 2],
                 [6, 5, 3, 3, 2],
                 [3, 3, 5, 4, 9],
                 [3, 5, 3, 9, 0]]
        self.assertEqual(TreeCounter().highest_scenic_score(value), 8)


if __name__ == '__main__':
    unittest.main()
