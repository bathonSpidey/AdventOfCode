class TreeCounter:

    def count(self, forest):
        total_trees = 2 * len(forest) + 2 * (len(forest[0]) - 2)
        for row in range(1, len(forest) - 1):
            for column in range(1, len(forest[0]) - 1):
                total_trees += self.add_tree(column, forest, row)
        return total_trees

    def add_tree(self, column, forest, row):
        current_tree = forest[row][column]
        left_neighbors = all(current_tree > num for num in forest[row][:column])
        right_neighbors = all(current_tree > num for num in forest[row][column + 1:])
        up_neighbors = all(current_tree > num for num in [row[column] for row in forest[:row]])
        down_neighbors = all(current_tree > num for num in [row[column] for row in forest[row + 1:]])
        if left_neighbors or right_neighbors or up_neighbors or down_neighbors:
            return 1
        return 0

