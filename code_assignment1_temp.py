from microbit import *

#calibrate the compass when the program starts
compass.calibrate

#main loop
while True:
    
    #Read temperature and place in variable
    temp = temperature()
    
    #Read compass heading and place in variable
    direction = compass.heading()
    
    #Display temp converted to Fahrenheit
    display.scroll(str(temp*(9/5)+32)+" Deg F")
    
    #Display compass heading
    display.scroll(str(direction))
    
    #Build CSV entry variable
    entry = (str(temp)) + ", " + (str(direction))
    
    #open csv on microbit
    with open('tempdir.csv') as csv:
        csv.write(entry)
    
    sleep(10000)
    
    #Print results to terminal
    print(entry)
