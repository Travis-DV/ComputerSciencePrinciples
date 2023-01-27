from random import randint #Imports only part of a library
ticketC = 75
isschool = randint(0,4)
ran = randint(0,3)
counter = 0
if input("Do you want to do your own numbers?").lower() == "y":
    speedlimit = int(input("What is the speedlimit"))
    yougo = int(input("How fast where you going?"))
    isschool = input("Was it in a school zone?").lower() == "y"
else:
    #set speedlimit based on a random number
    if 0 == ran:
        speedlimit = 25
    elif 1 == ran:
        speedlimit = 55
    elif 2 == ran:
        speedlimit = 30
    else:
        speedlimit = 10
    #sets how fast you were going to make ticket
    ran = randint(0,3)
    ran2 = randint(-5,15)
    if 0 == ran:
        yougo = 25+ran2
    elif 1 == ran:
        yougo = 55+ran2
    elif 2 == ran:
        yougo = 30+ran2
    else:
        yougo = 10+ran2
#Ditermin how much your ticket is if you are over or under
if yougo > speedlimit or yougo < speedlimit/4:
    print(f"You were going {yougo}, the Speedlimit is {speedlimit}.")
    if yougo > speedlimit:
        overam = yougo-speedlimit
        print(f"You were {overam} mph over the speedlimit")
        #incroments the cost based on how many 10s over you are
        ticketC += overam*6
        #checks if you were <30 over
        if 30 <= overam:
                print("You were more then 30 over")
                ticketC += 160
        #Checks if you were in a school zone
        if isschool == 1 or isschool:
            print("IN A SCHOOL ZONE!!!!")
            ticketC *= 2
        print(f"Your ticket is ${ticketC}.")
    else:
        undam = speedlimit-yougo
        print(f"You were {undam} mph under the speed limit.")
        undam = undam/4
        while 0 < undam:
            ticketC += 6
            undam -= 10
            counter += 1
        if 3 <= counter:
            ticketC += 160
        print(f"Your ticket is ${ticketC}.")
