import time
import random


def matrix_rain(text, speed=0.1, size=10):
    """Generates the matrix falling letters effect.

    Args:
      text: The text to be displayed.
      speed: The speed of the falling letters, in seconds per letter.
      size: The size of the letters, in pixels.

    Returns:
      A generator that yields the falling letters.
    """

    # Create a list of the letters in the text.
    letters = list(text)

    # Create a list of the positions of the letters.
    positions = []
    for i in range(len(letters)):
        positions.append([random.randint(0, size), random.randint(0, size)])

    # Start a loop that will run until all of the letters have fallen.
    while positions:
        # Clear the screen.
        print("\033[H\033[2J", end="")

        # Update the positions of the letters.
        for i, position in enumerate(positions):
            position[1] += speed

        # Remove any letters that have fallen off the screen.
        for i in range(len(positions) - 1, -1, -1):
            if positions[i][1] > size:
                positions.pop(i)

        # Print the letters at their new positions.
        for i, position in enumerate(positions):
            print(letters[i], end="", flush=True)

        # Wait for a short amount of time.
        time.sleep(speed)


if __name__ == "__main__":
    # Get the text to be displayed.
    text = input("Enter the text to be displayed: ")

    # Generate the falling letters.
    for letter in matrix_rain(text):
        pass
