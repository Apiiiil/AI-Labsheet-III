import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the Puzzle problem with an initial and goal state.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.n = len(goal_state)  # Size of the grid (3x3 for 8 puzzle)

    def heuristic(self, state):
        """
        Calculate the heuristic value (Manhattan Distance).
        Manhattan Distance is the sum of the distances of tiles from their goal positions.
        """
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                value = state[i][j]
                if value != 0:  # Ignore the blank tile (0)
                    # Find goal position of the current tile
                    goal_x, goal_y = divmod(self.goal_state.index(value), self.n)
                    current_x, current_y = i, j
                    distance += abs(goal_x - current_x) + abs(goal_y - current_y)
        return distance

    def get_neighbors(self, state):
        """
        Generate all possible moves from the current state by sliding the blank tile (0).
        """
        neighbors = []
        # Find the blank tile (0)
        x, y = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

        # Possible moves: Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:  # Check if the move is within bounds
                # Swap the blank tile with the target tile
                new_state = [row[:] for row in state]  # Deep copy the state
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)

        return neighbors

    def is_goal(self, state):
        """
        Check if the current state is the goal state.
        """
        return state == self.goal_state

    def solve(self):
        """
        Solve the 8 Puzzle Problem using the A* algorithm.
        """
        # Priority queue (min-heap)
        open_list = []
        # Closed list to track visited states
        closed_set = set()

        # Initial state with heuristic and cost
        initial_state = self.initial_state
        heapq.heappush(open_list, (self.heuristic(initial_state), 0, initial_state, None))

        # Parent mapping for reconstructing the path
        parent_map = {}

        while open_list:
            # Get the state with the lowest f = g + h
            _, cost, current_state, parent = heapq.heappop(open_list)

            # Check if the goal is reached
            if self.is_goal(current_state):
                parent_map[tuple(map(tuple, current_state))] = parent
                return self.reconstruct_path(parent_map, current_state)

            # If already visited, skip
            if tuple(map(tuple, current_state)) in closed_set:
                continue

            # Mark as visited
            closed_set.add(tuple(map(tuple, current_state)))

            # Add current state to parent map
            parent_map[tuple(map(tuple, current_state))] = parent

            # Generate neighbors and add them to the open list
            for neighbor in self.get_neighbors(current_state):
                if tuple(map(tuple, neighbor)) not in closed_set:
                    g_cost = cost + 1  # Increment cost for moving to the neighbor
                    f_cost = g_cost + self.heuristic(neighbor)
                    heapq.heappush(open_list, (f_cost, g_cost, neighbor, current_state))

        return None  # No solution found

    def reconstruct_path(self, parent_map, state):
        """
        Reconstruct the solution path from the parent map.
        """
        path = []
        while state is not None:
            path.append(state)
            state = parent_map[tuple(map(tuple, state))]
        return path[::-1]  # Reverse the path


# Driver Code
if __name__ == "__main__":
    # Initial state of the puzzle (0 represents the blank tile)
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    # Goal state of the puzzle
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Create Puzzle instance
    puzzle = Puzzle(initial_state, goal_state)

    # Solve the puzzle using A* algorithm
    solution = puzzle.solve()

    if solution:
        print("Solution found! Steps:")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")
