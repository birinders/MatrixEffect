from random import randint
from time import sleep, time
import colorama as cl
from colors import *
import os

# Disable text wrap
# Set the LINES environment variable to 0
# os.environ["LINES"] = "0"

# # Disable Auto Scroll
# os.environ["scrolloff"] = "0"


# Monospace letter sizes
letter_height = 20
letter_width = 10

##############################################################
######################### Settings ###########################
common_start = True


##############################################################
####################### GridDimensions #######################

grid_width = 150
grid_height = 80
grid_height = int(grid_height * letter_width // letter_height)

####################### GridDimensions #######################
##############################################################

#############################################################
####################### Color Configs #######################
cl_primary = cl_white
trail_prim = cl_lightgreen
trail_sec = cl_green
####################### Color Configs #######################
#############################################################

cl.init()
print("\033[?25l", end="")


def array_printer(arr):
    for x in arr:
        print(*x, sep="")


def move(y, x):
    print("\033[%d;%dH" % (y, x))


class Digit:
    def __init__(self, column, pos=0):
        self.column = column

        self.pos_float = pos
        self.pos = int(self.pos_float)
        self.speed = randint(70, 100)
        self.speed /= 200
        self.max_length = randint(int(0.2 * grid_height), int(0.7 * grid_height))

        self.letter = letters[randint(0, n_letters - 1)]

    def colour(self):
        color_len = self.max_length - 1
        sec_len = int(color_len * 0.4)
        prim_len = color_len - sec_len

        if self.pos < grid_height:
            ascii_grid[self.pos][self.column] = (
                cl_primary + og_grid[self.pos][self.column]
            )

        if self.pos - 1 < grid_height and self.pos - 1 >= 0:
            i = self.pos - 1

            # Color all the greens
            while i >= 0 and sec_len:
                ascii_grid[i][self.column] = trail_prim + og_grid[i][self.column]
                i -= 1
                sec_len -= 1
            while i >= 0 and prim_len:
                ascii_grid[i][self.column] = trail_sec + og_grid[i][self.column]
                i -= 1
                prim_len -= 1

        if self.pos >= grid_height:
            i = self.pos - self.max_length

            while i < grid_height and prim_len:
                ascii_grid[i][self.column] = trail_sec + og_grid[i][self.column]
                i += 1
                prim_len -= 1

            while i < grid_height and sec_len:
                ascii_grid[i][self.column] = trail_prim + og_grid[i][self.column]
                i += 1
                sec_len -= 1

        # if self.pos < grid_height:
        #     i = self.pos
        #     while i >= 0 and i < color_len:
        #         for i in range(min(grid_height, self.pos), max())
        #         ascii_grid[i][self.column] = cl.Fore.GREEN

    def update(self):
        self.last_pos = self.pos

        self.pos_float += self.speed
        self.pos = int(self.pos_float)

        # if letter is still same, randomly change it for next iteration
        if self.pos == self.last_pos and self.pos < grid_height:
            # self.colour()
            return
            # ascii_grid[self.pos][self.column] = letters[randint(0, n_letters - 1)]
            # og_grid[self.pos][self.column] = letters[randint(0, n_letters - 1)]

        # Reset string when completely finished and out of zone, exit
        if self.pos - self.max_length >= grid_height:
            self.__init__(randint(0, grid_width - 1))
            # self.colour()
            return

        # Clear remaining trail, exit
        if self.pos >= grid_height:
            ascii_grid[self.pos - self.max_length][self.column] = " "
            og_grid[self.pos - self.max_length][self.column] = " "
            # self.colour()
            return

        # Clear letters in between the screen
        if self.pos >= self.max_length:
            ascii_grid[self.pos - self.max_length][self.column] = " "
            og_grid[self.pos - self.max_length][self.column] = " "

        # If space allows, add a new letter
        # Character still on screen, update the position on the ascii grid
        self.letter = letters[randint(0, n_letters - 1)]
        ascii_grid[self.pos][self.column] = self.letter
        og_grid[self.pos][self.column] = self.letter

        # self.colour()


##### Avoid these character sets #####
hebrew = "אבגדהוזחטיכלמננסעפצקרשת"
korean = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅚㅛㅜㅠㅡㅢㅣ"
##### Avoid these character sets #####


greek = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
cyrillic = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
unique_english = "ůŭŧńşźżñçéáíóúàèìòùœžšžćčđłńó÷øðþæıȷȷłńó÷øðþæ"
kb_symbols = "~!@#$%^&*()_+-={}[]|\\;:<>?/"
english_letters = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
letters = greek + cyrillic + unique_english + kb_symbols + english_letters + numbers
# letters = "ぁぃぅぇぉっゃゅょひふへほまみむめもやゆよらりるれろわんにゃんみゃん"
n_letters = len(letters)

ascii_grid = [[" " for i in range(grid_width)] for j in range(grid_height)]
og_grid = [[" " for i in range(grid_width)] for j in range(grid_height)]


##### Initialize the grid #####
max_lines = int(grid_width * 0.8)

# start_height = 1 for common start
# start_height = grid_height for random start
start_height = 1 if common_start else grid_height
class_arr = [
    Digit(randint(0, grid_width - 1), randint(0, start_height - 1))
    for i in range(max_lines)
]

# Main loop
os.system("cls")

show_stats = False
frame_ctr = 0

target_fps = 60
seconds_per_frame = 1 / target_fps

start_t = time()
fps = 0

# Set the right command line size
os.system(f"mode con: cols={grid_width} lines={grid_height+2}")

while True:
    frame_ctr += 1
    frame_start_t = time()

    move(0, 0)

    for elem in class_arr:
        elem.update()
        elem.colour()

    end_t = time()
    dif = end_t - frame_start_t

    if dif > 0.001:
        inf_fps = 1 / dif
    else:
        inf_fps = "too high lol"
    if end_t - start_t > 1:
        fps = frame_ctr
        frame_ctr = 0
        start_t = time()

    if show_stats:
        print(f"{cl_primary}Target FPS = {target_fps}")
        print(f"{cl_primary}Uncapped FPS = {inf_fps}")
        print(f"{cl_primary}Smooth FPS = {fps}")
        print(
            f"{cl_primary}Target mSPF = {seconds_per_frame*1000}, Attained mSPF = {dif*1000}"
        )

    if dif < seconds_per_frame:
        sleep(seconds_per_frame - dif)
    print_start_t = time()
    array_printer(ascii_grid)
    print_end_t = time()

    # if show_stats:
    #     print(f"{cl_primary}Target FPS = {target_fps}")
    #     print(f"{cl_primary}Uncapped FPS = {inf_fps}")
    #     print(f"{cl_primary}Smooth FPS = {fps}")
    #     print(
    #         f"{cl_primary}Target mSPF = {seconds_per_frame*1000}, Attained mSPF = {dif*1000}"
    #     )
    # time_to_print = (
    #     (print_end_t - print_start_t) * 100 / dif
    #     if dif > 0.001
    #     else "divide by zero"
    # )
    # print(f"{cl_primary}{time_to_print}% time of frame build to render")
