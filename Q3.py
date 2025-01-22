from collections import deque

class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state  # Initial state (4-litre jug, 3-litre jug)
        self.goal_state = goal_state       # Goal state (4-litre jug, 3-litre jug)

    def goalTest(self, current_state):
        """Check if the current state matches the goal state."""
        return current_state == self.goal_state

    def successor(self, state):
        """
        Generate possible successors from the current state
        using the water jug problem rules.
        """
        successors = []
        jug1, jug2 = state  # jug1 = 4L jug, jug2 = 3L jug

        # Rule 1: Fill the 4-litre jug
        if jug1 < 4:
            successors.append((4, jug2))
        # Rule 2: Fill the 3-litre jug
        if jug2 < 3:
            successors.append((jug1, 3))
        # Rule 3: Empty the 4-litre jug
        if jug1 > 0:
            successors.append((0, jug2))
        # Rule 4: Empty the 3-litre jug
        if jug2 > 0:
            successors.append((jug1, 0))
        # Rule 5: Pour water from 4-litre to 3-litre jug until the latter is full or the former is empty
        transfer = min(jug1, 3 - jug2)
        if transfer > 0:
            successors.append((jug1 - transfer, jug2 + transfer))
        # Rule 6: Pour water from 3-litre to 4-litre jug until the latter is full or the former is empty
        transfer = min(jug2, 4 - jug1)
        if transfer > 0:
            successors.append((jug1 + transfer, jug2 - transfer))

        return successors

    def generate_path(self, closed, state):
        """Trace the path from the initial state to the goal state."""
        path = []
        while state is not None:
            path.append(state)
            state = closed[state]  # Backtrack using the parent information
        return path[::-1]  # Reverse the path

    def search(self, method="BFS"):
        """
        Perform search to find the solution.
        Supports DFS and BFS.
        """
        open_list = deque()  # Queue for BFS, Stack for DFS
        closed = {}  # Store visited states with parent
        open_list.append((self.initial_state, None))  # (state, parent)

        while open_list:
            if method == "BFS":
                current_state, parent = open_list.popleft()
            elif method == "DFS":
                current_state, parent = open_list.pop()

            # If the goal is found, return the solution path
            if self.goalTest(current_state):
                closed[current_state] = parent
                return self.generate_path(closed, current_state)

            # Add the current state to the closed list
            if current_state not in closed:
                closed[current_state] = parent
                # Add all unvisited successors to the open list
                for successor in self.successor(current_state):
                    if successor not in closed:
                        open_list.append((successor, current_state))

        return None  # If no solution is found


# Driver Code
if __name__ == "__main__":
    # Initial state: (4L jug, 3L jug) -> (4, 0)
    # Goal state: (4L jug, 3L jug) -> (2, x) where x is any value
    initial_state = (4, 0)
    goal_state = (2, 0)  # We aim to have exactly 2L in the 4L jug

    # Create WaterJug problem instance
    water_jug_problem = WaterJug(initial_state, goal_state)

    # Run BFS and print solution path
    print("Solving using BFS:")
    solution = water_jug_problem.search(method="BFS")
    if solution:
        print("Solution Path:", solution)
    else:
        print("No solution found.")

    print("\nSolving using DFS:")
    solution = water_jug_problem.search(method="DFS")
    if solution:
        print("Solution Path:", solution)
    else:
        print("No solution found.")
