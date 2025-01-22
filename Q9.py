import math
import random

def simulated_annealing(initial_state, objective_function, neighbor_function, temperature_schedule):
    """
    Perform simulated annealing to demonstrate the effect of temperature on selecting inferior nodes.

    Parameters:
    - initial_state: The starting state.
    - objective_function: Function to calculate the "quality" of a state.
    - neighbor_function: Function to generate a neighboring state.
    - temperature_schedule: Function to define the temperature at a given time step.

    Returns:
    - final_state: The state after the simulated annealing process.
    """
    current_state = initial_state
    current_value = objective_function(current_state)

    for time in range(1, 1000):  # Max number of iterations
        temperature = temperature_schedule(time)
        if temperature <= 0:
            break  # Stop if temperature becomes too low

        # Generate a neighboring state
        neighbor = neighbor_function(current_state)
        neighbor_value = objective_function(neighbor)

        # Calculate the change in value
        delta_value = neighbor_value - current_value

        # Decide whether to move to the neighbor
        if delta_value > 0 or random.random() < math.exp(delta_value / temperature):
            # Accept the move (even if inferior, based on probability)
            current_state = neighbor
            current_value = neighbor_value

        print(f"Time: {time}, Temperature: {temperature:.2f}, Current Value: {current_value}, Delta: {delta_value}")

    return current_state


def objective_function(state):
    """
    Example objective function: Maximize a simple quadratic function.
    f(x) = -(x-3)^2 + 10 (peaks at x = 3)
    """
    return -((state - 3) ** 2) + 10


def neighbor_function(state):
    """
    Generate a neighbor by making a small random move.
    """
    return state + random.uniform(-1, 1)


def temperature_schedule(time):
    """
    Temperature schedule: Decreases over time.
    Example: T(t) = 100 / (1 + t)
    """
    return 100 / (1 + time)


# Driver Code
if __name__ == "__main__":
    # Initial state
    initial_state = random.uniform(0, 10)  # Start with a random value between 0 and 10

    # Run simulated annealing
    print("Simulated Annealing:")
    final_state = simulated_annealing(
        initial_state=initial_state,
        objective_function=objective_function,
        neighbor_function=neighbor_function,
        temperature_schedule=temperature_schedule
    )

    print(f"\nFinal State: {final_state}")
    print(f"Final Value: {objective_function(final_state)}")
