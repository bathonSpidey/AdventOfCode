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

    def highest_scenic_score(self, forest):
        highest_scenic_score = 0
        for row in range(1, len(forest) - 1):
            for column in range(1, len(forest[0]) - 1):
                vision_score = self.view_score(column, forest, row)
                if vision_score > highest_scenic_score:
                    highest_scenic_score = vision_score
        return highest_scenic_score

    def view_score(self, column, forest, row):
        current_tree = forest[row][column]
        left_view = self.total_trees(current_tree, forest[row][:column][::-1])
        right_view = self.total_trees(current_tree, forest[row][column + 1:])
        top_view = self.total_trees(current_tree, [row[column] for row in forest[:row][::-1]])
        bottom_view = self.total_trees(current_tree, [row[column] for row in forest[row + 1:]])
        return left_view * right_view * top_view * bottom_view

    def total_trees(self, tree_height, tree_list):
        count = 0
        for index, tree in enumerate(tree_list):
            count = index + 1
            if tree >= tree_height:
                return count
        return count




