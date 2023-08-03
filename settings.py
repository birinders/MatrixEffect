from inits import *

# Monospace letter sizes
letter_height = 20
letter_width = 10

####################### GridDimensions #######################
grid_width = 160
grid_height = 100
grid_height = int(grid_height * letter_width // letter_height)


####################### Color Configs ########################
cl_primary = cl_white
trail_prim = cl_lightgreen
trail_sec = cl_green


######################### General ############################
common_start = False
max_lines = int(grid_width * 0.8)

######################## Debugging ###########################
show_stats = False
match_target = False
window_threshold = 4500
