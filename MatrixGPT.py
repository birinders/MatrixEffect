import random
import time

# The great failures of AI

# List of characters to be used for the falling effect
characters = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
# Terminal dimensions (manually set the values)
rows = 30
columns = 80

# Initialize the matrix
matrix = []
for _ in range(columns):
    matrix.append([random.choice(characters), 0])


# Function to update the matrix
def update_matrix():
    for i in range(columns):
        character, count = matrix[i]
        if count > 0:
            matrix[i] = [character, count - 1]
        else:
            matrix[i] = [random.choice(characters), random.randint(5, 15)]


# Function to display the matrix
def display_matrix():
    for row in range(rows):
        for col in range(columns):
            character, _ = matrix[col]
            if row == rows - 1:
                print(character)
            else:
                print(character, end="")
    print("\033[H")


# Main loop
while True:
    update_matrix()
    display_matrix()
    time.sleep(0.1)  # Adjust the sleep duration to change the falling speed
