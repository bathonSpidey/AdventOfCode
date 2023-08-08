import unittest


class TreeCounter:

    def Count(self, grid):
        rows={}
        cols={}
        for i, row in enumerate(grid):
            rows[i] = row
        for j in range(len(grid[0])):
            cols[j] = [grid[i][j] for i in range(len(grid))]
        total_tres = 2 * len(grid) + 2 * (len(grid[0]) - 2)
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                value = grid[i][j]
                leftRowList= rows[i][0:j]
                rightRowList = rows[i][j+1:]
                upNeihbors = cols[j][0:i]
                downNeigbors = cols[j][i+1:]
                if all(value > num for num in leftRowList) or all(value > num for num in rightRowList) or all(value > num for num in upNeihbors) or all(value > num for num in downNeigbors):
                    total_tres += 1

        return total_tres





class TreeCounterTests(unittest.TestCase):
    def test_edge_trees_should_be_counted(self):
        tests = [
            ([[1, 2, 3], [4, 1, 5], [6, 7, 8]], 8),
            ([[0, 0, 0, 0, 0]] * 5, 16)
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(TreeCounter().Count(value), expected)

    def test_small_forest_with_no_cover(self):
        tests = [
            ([[1, 2], [3, 4]], 4),
            ([[1, 2, 3], [4, 9, 5], [6, 7, 8]], 9),
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(TreeCounter().Count(value), expected)

    def test_given_case(self):
        value= [[3, 0, 3, 7, 3],
         [2, 5, 5, 1, 2],
         [6, 5, 3, 3, 2],
         [3, 3, 5, 4, 9],
         [3, 5, 3, 9, 0]]
        self.assertEqual(TreeCounter().Count(value), 21)


if __name__ == '__main__':
    unittest.main()
