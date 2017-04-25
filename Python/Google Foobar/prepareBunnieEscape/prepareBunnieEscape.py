from collections import deque


class Node:

    def __init__(self, x, y, gren, grid):
        self.x = x
        self.y = y;
        self.gren = gren # this keeps track of the wall removal, with a
        # limit of one use set for 'source' in GridEscapeRouter
        self.grid = grid

    def __hash__(self):
        return self.x ^ self.y
        # use of this hash method allows for a much MUCH quicker comparison
        # of dictionary keys.

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.gren == other.gren 
        # explicitly defining the eq method allows you to establish which
        # object properties will be evaluated when determining if two objects
        # are equal. the __eq__ and __hash__ methods are linked in
        # their purporse of optimizing the runtime.

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        gren = self.gren
        grid = self.grid
        rows = len(grid)
        columns = len(grid[0])

        # here we get to know the neighbors!
        if x > 0: # if x pos is closed then go back
            wall = grid[y][x - 1] == 1
            if wall:
                if gren > 0: # if you can still move walls then do it!
                    neighbors.append(Node(x - 1, y, gren - 1, grid))
            else:
                neighbors.append(Node(x - 1, y, gren, grid))

        if x < columns - 1: # if x pos is open then go to the next
            # to the right
            wall = grid[y][x + 1] == 1
            if wall:
                if gren > 0:
                    neighbors.append(Node(x + 1, y, gren - 1, grid))
            else:
                neighbors.append(Node(x + 1, y, gren, grid))

        if y > 0: # if y pos is closed then go back
            wall = grid[y - 1][x] == 1
            if wall:
                if gren > 0:
                    neighbors.append(Node(x, y - 1, gren - 1, grid))
            else:
                neighbors.append(Node(x, y - 1, gren, grid))

        if y < rows - 1: # if y pos is open then go to the next one
            # down
            wall = grid[y + 1][x]
            if wall:
                if gren > 0:
                    neighbors.append(Node(x, y + 1, gren - 1, grid))
            else:
                neighbors.append(Node(x, y + 1, gren, grid))

        return neighbors


class GridEscapeRouter:

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])

    def get_escape_route_length(self):
        source = Node(0, 0, 1, self.grid) # gren is set to one since the
        # challenge restricts it to one moveable wall
        queue = deque([source]) # the deque sequence allows the popleft()
        # method which is faster than the pop() method for a list.
        distance_map = {source: 1} # dictionary with source as key and
        # 1 as value

        while queue:
            current_node = queue.popleft()

            if current_node.x == self.columns - 1 and\
                current_node.y == self.rows - 1: 
                return distance_map[current_node]

            for child_node in current_node.get_neighbors():
                if child_node not in distance_map.keys():
                    distance_map[child_node] = distance_map[current_node] + 1
                    queue.append(child_node)

        return 1000 * 1000 * 1000 # situations where there's no escape!

def answer(maze):
    router = GridEscapeRouter(maze)
    route_length = router.get_escape_route_length();

    print("Route length: ", route_length)
    return route_length


print(answer([[0, 1, 1, 0],
               [0, 0, 0, 1],
               [1, 1, 0, 0],
               [1, 1, 1, 0]]))
print(answer([[0, 1, 1, 0],
               [0, 1, 1, 1],
               [1, 1, 1, 0],
               [1, 1, 1, 0]]))
"""print(answer([[0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))"""
