import random

class ReflexVacuumCleaner:
    def __init__(self):
        # Initialize the environment with two rooms (A and B) and their statuses (clean/dirty)
        self.environment = {
            'A': random.choice(['clean', 'dirty']),
            'B': random.choice(['clean', 'dirty'])
        }
        self.current_position = random.choice(['A', 'B'])  # Vacuum starts at a random position

    def sense_environment(self):
        # Sense the status of the current room
        return self.environment[self.current_position]

    def clean(self):
        # Clean the current room
        print(f"Cleaning room {self.current_position}")
        self.environment[self.current_position] = 'clean'

    def move(self):
        # Move to the other room
        next_position = 'A' if self.current_position == 'B' else 'B'
        print(f"Moving from room {self.current_position} to room {next_position}")
        self.current_position = next_position

    def display_environment(self):
        # Display the current state of the environment
        print(f"Environment: {self.environment}")
        print(f"Vacuum is in room {self.current_position}")

    def run(self):
        # Execute the reflex agent's behavior
        print("Starting the vacuum cleaner...")
        steps = 0
        while 'dirty' in self.environment.values():
            self.display_environment()
            status = self.sense_environment()
            if status == 'dirty':
                self.clean()
            else:
                self.move()
            steps += 1
        print("All rooms are clean!")
        print(f"Total steps taken: {steps}")

# Run the Reflex Vacuum Cleaner
if __name__ == "__main__":
    vacuum = ReflexVacuumCleaner()
    vacuum.run()
