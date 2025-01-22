def calculate_heuristic(state, goal_state):
    """
    Calculate the heuristic value of the given state for the Blocks World Problem.
    
    Parameters:
    - state: Current state of the blocks, represented as a list of stacks.
    - goal_state: Goal state of the blocks, represented as a list of stacks.
    
    Returns:
    - heuristic_value: An integer representing the heuristic value of the state.
    """
    heuristic_value = 0

    # Create a dictionary mapping each block to its correct support in the goal state
    correct_support = {}
    for stack in goal_state:
        for i in range(len(stack) - 1):
            correct_support[stack[i]] = stack[i + 1]
        if stack:
            correct_support[stack[-1]] = None  # The last block in a stack has no support

    # Evaluate the heuristic for the current state
    for stack in state:
        for i in range(len(stack) - 1):
            current_block = stack[i]
            support_block = stack[i + 1]
            # Check if the current block has the correct support
            if correct_support.get(current_block) == support_block:
                # Correct support structure: +1 for every block in the structure
                heuristic_value += (len(stack) - i)
            else:
                # Incorrect support structure: -1 for every block in the structure
                heuristic_value -= (len(stack) - i)

        # Handle the last block in the stack
        if stack:
            last_block = stack[-1]
            if correct_support.get(last_block) is None:
                # Correct support for the last block
                heuristic_value += 1
            else:
                # Incorrect support for the last block
                heuristic_value -= 1

    return heuristic_value


# Driver Code
if __name__ == "__main__":
    # Example: Initial and goal states
    initial_state = [
        ['A', 'B'],  # Stack 1
        ['C'],       # Stack 2
        []           # Stack 3
    ]

    goal_state = [
        ['C', 'B', 'A'],  # Stack 1
        [],
        []
    ]

    # Calculate heuristic value
    heuristic_value = calculate_heuristic(initial_state, goal_state)
    print(f"Heuristic Value for the initial state: {heuristic_value}")
