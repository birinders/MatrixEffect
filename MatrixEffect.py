from random import randint
from time import sleep
import winsound
import colorama as cl
import os

cl.init()
print("\033[?25l", end="")


def array_printer(arr):
    for x in arr:
        print(*x, sep="")


def move(y, x):
    print("\033[%d;%dH" % (y, x))


class Digit:
    def __init__(self, column, index=None):
        self.column = column

        self.pos_float = 0
        self.pos = int(self.pos_float)
        self.speed = randint(7, 10)
        self.speed /= 15
        self.max_length = randint(int(0.2 * grid_height), int(0.7 * grid_height))

        self.letter = letters[randint(0, n_letters - 1)]
        self.index = index

    def __del__(self):
        pass
        # winsound.PlaySound("*", winsound.SND_ALIAS)

    def update(self):
        self.last_pos = self.pos

        self.pos_float += self.speed
        self.pos = int(self.pos_float)

        # if letter is still same, randomly change it for next iteration
        if self.pos == self.last_pos and self.pos < grid_height:
            ascii_grid[self.pos][self.column] = letters[randint(0, n_letters - 1)]
            return

        # Reset string when completely finished and out of zone, exit
        if self.pos - self.max_length >= grid_height:
            self.__init__(randint(0, grid_width - 1))
            return

        # Clear letters that are too long, exit
        if self.pos >= grid_height:
            ascii_grid[self.pos - self.max_length][self.column] = " "
            # ascii_grid[grid_height - 1][self.column] = ascii_grid[grid_height - 2][
            #     self.column
            # ]
            return

        # Clear letters in between the screen
        if self.pos >= self.max_length:
            ascii_grid[self.pos - self.max_length][self.column] = " "

        # Update the position on the ascii grid
        self.letter = letters[randint(0, n_letters - 1)]
        ascii_grid[self.pos][self.column] = self.letter


letter_height = 20
letter_width = 10

grid_width = 80
grid_height = 70
grid_height = int(grid_height * letter_width // letter_height)


letters = "0123456789"
# letters = "ぁぃぅぇぉっゃゅょひふへほまみむめもやゆよらりるれろわんにゃんみゃん"
# letters = "人犬猫鳥魚木山川海空"

n_letters = len(letters)

ascii_grid = [[" " for i in range(grid_width)] for j in range(grid_height)]

digit = Digit(10)

ascii_grid[0][10] = digit.letter

##### Initialize the grid #####
max_lines = int(grid_width * 0.8)
# max_lines = 10
class_arr = [Digit(randint(0, grid_width - 1), i) for i in range(max_lines)]
for elem in class_arr:
    ascii_grid[0][elem.column] = elem.letter

# Main loop
os.system("cls")
frame_ctr = 0
while True:
    move(0, 0)
    array_printer(ascii_grid)
    # digit.update()

    ##### Update all elements #####
    # print("Updating all values")
    # map(lambda digit: digit.update(), class_arr)
    for elem in class_arr:
        elem.update()
    # print(f"\n\n{frame_ctr}")
    # frame_ctr += 1

    # print(class_arr[0].pos)

    sleep(0.05)

    # print(f"\n\n{digit.pos}")
