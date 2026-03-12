# Simple Reflex Agent for Vacuum Cleaner World

# Function to simulate the vacuum cleaner agent
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Test the reflex agent
# Environment: location A is dirty, location B is clean
location = "A"
status = "Dirty"

# Agent's action
action = reflex_vacuum_agent(location, status)
print(f"Location: {location}, Status: {status}, Action: {action}")


# -----------------------------------------------------------------------------------------------------------------------

# 2)

# Simple Reflex Agent for Vacuum Cleaner World

# Function to simulate the vacuum cleaner agent
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Test the reflex agent
# Environment: location A is dirty, location B is clean initially
location = "A"
status = "Dirty"

# Define locations
locations = ["A", "B"]

# Simulate agent actions
for _ in range(5):  # Simulate for 5 iterations
    # Agent's action
    action = reflex_vacuum_agent(location, status)
    print(f"Location: {location}, Status: {status}, Action: {action}")

    # Update status
    if action == "Suck":
        status = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

# --------------------------------------------------------------------------------------------------------------------------
# 3)

def move_towards_goal(position, goal):
    while position < goal:
        position += 1
        print(f"Current Position: {position}")
    print("Reached the goal!")

# Set initial position and goal position
initial_position = 0
goal_position = 5

# Move towards the goal
move_towards_goal(initial_position, goal_position)

# ------------------------------------------------------------------------------------------------------------
# 4)

# Rational Agent to move towards a goal

class RationalAgent:
    def __init__(self, goal):
        self.position = 0
        self.goal = goal
    
    def move_towards_goal(self):
        while self.position < self.goal:
            self.position += 1
            print(f"Current Position: {self.position}")
        print("Reached the goal!")

# Set a goal position
goal_position = 5

# Create a rational agent
agent = RationalAgent(goal_position)

# Move the agent towards the goal
agent.move_towards_goal()

import random

# Function to display the room
def display(room):
    print(room)

# Initialize the room as a 4x4 grid, all elements set to 1 (dirty)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooms are dirty")
display(room)

# Randomly dirty some rooms
x = 0  # Initialize the row index
y = 0  # Initialize the column index

while x < 4:  # Loop over each row
    while y < 4:  # Loop over each column in the current row
        # Randomly choose 0 (clean) or 1 (dirty) for the current cell
        room[x][y] = random.choice([0, 1])
        y += 1  # Move to the next column
    x += 1  # Move to the next row
    y = 0  # Reset the column index to start from 0 for the next row

print("Before cleaning the room, I detect all of these random dirts")
display(room)

# Initialize counters for the cleaning process
x = 0  # Initialize the row index
y = 0  # Initialize the column index
z = 0  # Counter for the number of dirty cells cleaned

# Clean the room
while x < 4:  # Loop over each row
    while y < 4:  # Loop over each column in the current row
        if room[x][y] == 1:  # If the current cell is dirty
            print("Vacuum in this location now:", x, y)
            room[x][y] = 0  # Clean the current cell
            print("Cleaned:", x, y)
            z += 1  # Increment the counter for cleaned cells
        y += 1  # Move to the next column
    x += 1  # Move to the next row
    y = 0  # Reset the column index to start from 0 for the next row

# Calculate the performance percentage
performance = (100 - ((z / 16) * 100))
print("Room is clean now. Thanks for using the Robot Vacuum Cleaner!")
display(room)
print('Performance=', performance, '%')

# --------------------------------------------------------------------------------------------------

