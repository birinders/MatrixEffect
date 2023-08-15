from inits import *

# Monospace letter sizes
letter_height = 20
letter_width = 10

####################### GridDimensions #######################
grid_width = 120
grid_height = 60
grid_height = int(grid_height * letter_width // letter_height)


####################### Color Configs ########################
cl_primary = cl_white
trail_prim = cl_lightgreen
trail_sec = cl_green


######################### General ############################
speed_factor = 250
# The higher the factor, the lower the speed
# Avoid reducing below 100

common_start = False
max_lines = int(grid_width * 0.8)
# max_lines = 400

######################## Debugging ###########################
show_stats = False
match_target = False
window_threshold = 4500
