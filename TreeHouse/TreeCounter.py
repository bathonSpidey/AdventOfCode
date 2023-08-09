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
        score=1
        previous_score=1
        left_view=0

        for row in range(1, len(forest) - 1):
            for column in range(1, len(forest[0]) - 1):
                current_tree = forest[row][column]
                if  not self.add_tree(column, forest, row):
                    for num in forest[row][:column]:
                        if num < current_tree:
                            left_view += 1

    def count_views(self, neighbors, current_tree ):
        count=0
        for tree in neighbors:
            if tree<current_tree:
                count+=1
        return count




