import math
from pico 2d import *

open_canvas()

grass = load_image('grass.png')
charactoer = load_image('character.png')

while True:
    run_circle()
    run_rectangle()
close_canvas()
