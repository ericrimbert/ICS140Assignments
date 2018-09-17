# 2.9.2 - Tree height

# imports tan from math module
from math import tan

# variables that set the angle elevation and the shadow length
angle_elev = 3.8
shadow_len = 17.5

# tree height
tree_height = tan(angle_elev) * shadow_len

# prints the tree height
print(f"Tree height is: {tree_height}.")
