import random

class Puzzle:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the 8-puzzle problem with the given initial and goal states.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.n = len(goal_state)  # Size of the grid (3x3 for 8-puzzle)

    def heuristic(self, state):
        """
        Calculate the heuristic value using Manhattan Distance.
        """
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                value = state[i][j]
                if value != 0:  # Ignore the blank tile (0)
                    # Find the target position of the current tile in the goal state
                    goal_x, goal_y = divmod(self.goal_state.index(value), self.n)
                    current_x, current_y = i, j
                    distance += abs(goal_x - current_x) + abs(goal_y - current_y)
        return distance

    def get_neighbors(self, state):
        """
        Generate all possible neighbors of the current state by sliding the blank tile.
        """
        neighbors = []
        # Find the blank tile (0)
        x, y = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

        # Possible moves: Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:  # Check bounds
                # Create a new state by swapping the blank tile
                new_state = [row[:] for row in state]  # Deep copy
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)

        return neighbors

    def is_goal(self, state):
        """
        Check if the current state is the goal state.
        """
        return state == self.goal_state

    def steepest_ascent(self):
        """
        Solve the 8-puzzle problem using Steepest Ascent Hill Climbing.
        """
        current_state = self.initial_state
        current_heuristic = self.heuristic(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            best_neighbor = None
            best_heuristic = float("inf")

            # Evaluate each neighbor and choose the best one
            for neighbor in neighbors:
                neighbor_heuristic = self.heuristic(neighbor)
                if neighbor_heuristic < best_heuristic:
                    best_neighbor = neighbor
                    best_heuristic = neighbor_heuristic

            # If no better neighbor is found, return the current state
            if best_heuristic >= current_heuristic:
                return current_state, current_heuristic

            # Move to the best neighbor
            current_state = best_neighbor
            current_heuristic = best_heuristic

    def print_state(self, state):
        """
        Print the current state of the puzzle in a readable format.
        """
        for row in state:
            print(row)
        print()


# Driver Code
if __name__ == "__main__":
    # Initial state of the puzzle
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

    # Flatten the goal state for heuristic calculation
    goal_state_flat = [val for row in goal_state for val in row]

    # Create the Puzzle instance
    puzzle = Puzzle(initial_state, goal_state_flat)

    # Solve the puzzle using Steepest Ascent Hill Climbing
    print("Initial State:")
    puzzle.print_state(initial_state)

    final_state, final_heuristic = puzzle.steepest_ascent()

    print("Final State (Local Optimum):")
    puzzle.print_state(final_state)

    if puzzle.is_goal(final_state):
        print("Goal state reached!")
    else:
        print("Local optimum reached. Heuristic:", final_heuristic)
