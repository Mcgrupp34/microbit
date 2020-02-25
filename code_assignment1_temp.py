from microbit import *

compass.calibrate

while True:
    temp = temperature()
    direction = compass.heading()
    display.scroll(str(temp*(9/5)+32)+" Deg F")
    display.scroll(str(direction))
    entry = (str(temp)) + ", " + (str(direction))
    with open('tempdir.csv') as csv:
        csv.write(entry)
    sleep(10000)
    print(entry)