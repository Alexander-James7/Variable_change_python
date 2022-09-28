from microbit import *

# Created by: Alexander James
# Date: 9/28/2022
# This automatically resets the variable to 0 on start
hungryness = 0
# This code tells the variable to increase the variable by 1 when 'A' is pressed and also to show the value
# It also resest the variable to 0 when 'B' is pressed
def on_forever():
    global hungryness
    if input.button_is_pressed(Button.A):
        hungryness = hungryness + 1
        basic.show_(hungryness)
    elif input.button_is_pressed(Button.B):
        hungryness = 0
        basic.show_number(hungryness)
    basic.forever(on_forever)
