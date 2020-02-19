from microbit import *
import random

#list of single digit options for the game, single digits used due to screen size
options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#initial start message
while True:
    display.scroll("Play Odd or Even!")
    display.clear()
    sleep(500)
    #option to start the game or reset
    display.scroll("Press A to start or B to reset")
    sleep(2000)

    if (button_a.was_pressed()):
        display.scroll("Press A if the # is even, B if the # is odd")
        display.scroll("Go!")
        #main game loop
        while True:

            #random sample of one integer from the options list
            num = random.choice(options)
            display.show(str(num))

            #user has two seconds to answer
            sleep(2000)

            #if number is even and A is pressed, they get happy face
            if (num % 2 == 0) and (button_a.was_pressed()):
                display.show(Image.HAPPY)

            #if number is even and B is pressed, they get skull
            elif (num % 2 == 0) and (button_b.was_pressed()):
                display.show(Image.SKULL)

            #if number is odd and B is pressed, they get happy face
            elif (num % 2 != 0) and (button_b.was_pressed()):
                display.show(Image.HAPPY)

            #if number is odd and A is pressed, they get skull
            elif (num % 2 != 0) and (button_a.was_pressed()):
                display.show(Image.SKULL)

            #outcome displays for two seconds before restarting
            sleep(2000)
            display.clear()

    #returns to start message
    elif (button_b.was_pressed()):
        display.clear()
        sleep(2000)