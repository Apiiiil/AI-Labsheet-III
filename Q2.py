import random

class ModelBasedVacuumCleaner:
    def __init__(self):
        # Initialize the environment with two rooms (A and B) and their statuses (clean/dirty)
        self.environment = {
            'A': random.choice(['clean', 'dirty']),
            'B': random.choice(['clean', 'dirty'])
        }
        self.current_position = random.choice(['A', 'B'])  # Vacuum starts at a random position
        
        # Agent's internal model of the environment (initially unknown)
        self.model = {
            'A': None,
            'B': None
        }

    def sense_environment(self):
        # Sense the status of the current room
        return self.environment[self.current_position]

    def update_model(self):
        # Update the internal model with the current room's status
        self.model[self.current_position] = self.sense_environment()

    def clean(self):
        # Clean the current room
        print(f"Cleaning room {self.current_position}")
        self.environment[self.current_position] = 'clean'
        self.model[self.current_position] = 'clean'

    def move(self):
        # Move to the other room
        next_position = 'A' if self.current_position == 'B' else 'B'
        print(f"Moving from room {self.current_position} to room {next_position}")
        self.current_position = next_position

    def display_status(self):
        # Display the current state of the environment and agent's model
        print(f"Environment: {self.environment}")
        print(f"Model: {self.model}")
        print(f"Vacuum is in room {self.current_position}")

    def run(self):
        # Execute the model-based agent's behavior
        print("Starting the model-based vacuum cleaner...")
        steps = 0
        while 'dirty' in self.environment.values():
            self.display_status()
            
            # Sense and update the model
            self.update_model()
            
            if self.model[self.current_position] == 'dirty':
                self.clean()
            else:
                # Only move if the other room might still be dirty
                other_room = 'A' if self.current_position == 'B' else 'B'
                if self.model[other_room] != 'clean':
                    self.move()
            steps += 1
        print("All rooms are clean!")
        print(f"Total steps taken: {steps}")

# Run the Model-Based Vacuum Cleaner
if __name__ == "__main__":
    vacuum = ModelBasedVacuumCleaner()
    vacuum.run()
