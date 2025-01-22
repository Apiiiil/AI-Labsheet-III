from collections import deque

class BlockWorld:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the BlockWorld problem with an initial and goal state.
        Each state is represented as a list of stacks.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goalTest(self, current_state):
        """
        Check if the current state matches the goal state.
        """
        return current_state == self.goal_state

    def successor(self, state):
        """
        Generate possible successors from the current state by moving one block
        from the top of a stack to another stack.
        """
        successors = []
        num_stacks = len(state)

        for i in range(num_stacks):  # Iterate through all stacks
            if not state[i]:  # Skip empty stacks
                continue
            for j in range(num_stacks):  # Try to move the block to all other stacks
                if i != j:
                    # Create a deep copy of the state
                    new_state = [stack[:] for stack in state]
                    # Move the top block from stack i to stack j
                    block = new_state[i].pop()
                    new_state[j].append(block)
                    successors.append(new_state)

        return successors

    def generate_path(self, closed, state):
        """
        Trace the path from the initial state to the goal state.
        """
        path = []
        while state is not None:
            path.append(state)
            state = closed[state]  # Backtrack using the parent information
        return path[::-1]  # Reverse the path

    def state_to_tuple(self, state):
        """
        Convert a state (list of lists) to a tuple of tuples for hashing purposes.
        """
        return tuple(tuple(stack) for stack in state)

    def search(self, method="BFS"):
        """
        Perform search to find the solution. Supports DFS and BFS.
        """
        open_list = deque()  # Queue for BFS, Stack for DFS
        closed = {}  # Store visited states with parent

        # Convert initial state to tuple for hashing and add to open list
        open_list.append((self.state_to_tuple(self.initial_state), None))

        while open_list:
            if method == "BFS":
                current_state, parent = open_list.popleft()
            elif method == "DFS":
                current_state, parent = open_list.pop()

            # If the goal is found, return the solution path
            if self.goalTest(list(map(list, current_state))):
                closed[current_state] = parent
                return self.generate_path(closed, current_state)

            # Add the current state to the closed list
            if current_state not in closed:
                closed[current_state] = parent
                # Generate successors and add unvisited ones to the open list
                for successor in self.successor(list(map(list, current_state))):
                    successor_tuple = self.state_to_tuple(successor)
                    if successor_tuple not in closed:
                        open_list.append((successor_tuple, current_state))

        return None  # If no solution is found


# Driver Code
if __name__ == "__main__":
    # Initial state: 3 stacks
    initial_state = [
        ['A', 'B'],  # Stack 1
        ['C'],       # Stack 2
        []           # Stack 3
    ]

    # Goal state: Rearrange into a single stack
    goal_state = [
        ['C', 'B', 'A'],  # Stack 1
        [],
        []
    ]

    # Create BlockWorld problem instance
    block_world_problem = BlockWorld(initial_state, goal_state)

    # Run BFS and print solution path
    print("Solving using BFS:")
    solution = block_world_problem.search(method="BFS")
    if solution:
        print("Solution Path:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

    print("\nSolving using DFS:")
    solution = block_world_problem.search(method="DFS")
    if solution:
        print("Solution Path:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
