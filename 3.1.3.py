cost = 0.0 #added with iteration 2
sandwich_picked = 0 #added with iteration 3
drink_picked = 0 #added with iteration 3
fries_picked = 0 #added with iteration 3
words = []
word = "You want a "
sml = "Do you want a \033[1;36mSmall\033[1;0m $1 \033[1;36m(1)\033[1;0m,\n\033[1;33mMedium\033[1;0m $1.75 \033[1;33m(2)\033[1;0m,\nor \033[1;32mLarge\033[1;0m $2.25 \033[1;32m(3)\033[1;0m "
index2 = 0

# black = "30m"
# red = "31m" u
# green = "32m"
# yellow = "33m" u
# blue = "34m"
# magenta = "35m" u
# cyan = "36m" u
# white = "37m"

#iteration 1
    #gets what they want
    #Figures out what they told the program then tells them
def Sandwhich(words, cost):
    while True:
        input2 = str.lower(input("\033[1;33mChicken\033[1;0m $5.25 \033[1;33m(1)\033[1;0m, \n\033[1;35mBeef\033[1;0m $6.25 \033[1;35mBeef(2)\033[1;0m, \n\033[1;37mTofu\033[1;0m $5.75 \033[1;37m(3)\033[1;0m;\n\033[1;33m1\033[1;0m, \033[1;35m2\033[1;0m, or \033[1;37m3\033[1;0m if you are \033[1;31mdone\033[1;0m type \033[1;31m4\033[1;0m.\n"))
        if input2 == "1" or "c" in input2:
            print("You want a \033[1;33mChicken\033[1;0m Sandwich for $5.25")
            cost += 5.25
            words.append("\033[1;32mChicken Sandwich\033[1;0m")
        elif input2 == "2" or "b" in input2:
            print("You want a \033[1;35mBeef\033[1;0m Sandwich for $6.25")
            cost += 6.25
            words.append("\033[1;32mBeef Sandwich\033[1;0m")
        elif "3" == input2 or "t" in input2:
            print("You want a \033[1;37mTofu\033[1;0m Sandwich for $5.75")
            cost += 5.75
            words.append("\033[1;32mTofu Sandwich\033[1;0m")
        elif input2 == "4" or "d" in input2:
            sandwich_picked = 1
            break
        else:
            print("\033[1;31mError, try inputing again\033[1;0m")
    return sandwich_picked,cost,words
#Iteration 2
    #figure out if they want a drink or not
def drinks(cost, words, sml):
    while True:
    #Get what they want
        input2 = str.lower(input(sml + "Drink?;\n\033[1;36m1\033[1;0m, \033[1;33m2\033[1;0m, or \033[1;32m3\033[1;0m if you are \33[1;31mdone\033[1;0m type \033[1;31m4\033[1;0m.\n"))
    #fingure out what they told the system
        if input2 == "1" or "s" in input2:
            print("You want a \033[1;36mSmall\033[1;0m Drink for $1")
            cost += 1.00
            words.append("\033[1;34mSmall Drink\033[1;0m")
        elif input2 == "2" or "m" in input2:
            print("You want a \033[1;34mMedium\033[1;0m Drink for $1.75")
            cost += 1.75
            words.append("\033[1;34mMedium Drink\033[1;0m")
        elif "3" == input2 or "l" in input2:
            print("You want a \033[1;32mLarge\033[1;0m Drink for $2.25")
            cost += 2.25
            words.append("\033[1;34mLarge Drink\033[1;0m")
        elif input2 == "4" or "d" in input2 and "drink" not in input2:
            drink_picked = 1
            break
        else:
            print("\033[1;31mError, try inputing again\033[1;0m")
    return drink_picked,cost,words
def frys(cost, words, sml):
    while True:
#fingure out what they told the system
        input2 = str.lower(input(sml + "Fry?;\n\033[1;36m1\033[1;0m, \033[1;33m2\033[1;0m, or \033[1;32m3\033[1;0m if you are \033[1;31mdone\033[1;0m type \033[1;31m4\033[1;0m.\n"))
        if input2 == "1" or "s" in input2:
            while True:
                input2 = str.lower(input("Would you like to \033[1;33mMEGA-SIZE\033[1;0m that? \033[1;33my\033[1;0m, \033[1;31mn\033[1;0m \n"))
                if "y" in input2:
                    print("You want a \033[1;33mMEGA-SIZED\033[1;0m Fry for $2")
                    cost += 2.25
                    words.append("\033[1;33mMEGA-SIZED FRY!!!\033[1;0m")
                    break
                elif "n" in input2:
                    print("You want a \033[1;36mSmall\033[1;0m Fry for $1")
                    cost += 1.00
                    words.append("\033[1;33mSmall Fry\033[1;0m")
                    break
                else:
                    print("\033[1;31mError, try inputing again\033[1;0m")
        elif input2 == "2" or "m" in input2:
            print("You want a \033[1;34mMedium Fry\033[1;0m for $1.75")
            cost += 1.50
            words.append("\033[1;33mMedium Fry\033[1;0m")
        elif input2 == "3" or "l" in input2:
            print("You want a \033[1;32mLarge Fry for $2\033[1;0m")
            cost += 2.25
            words.append("\033[1;33mLarge Fry\033[1;0m")
        elif input2 == "4" or "d" in input2:
            fries_picked = 1
            break
        else:
            print("\033[1;31mError, Try inputing again!\033[1;0m")
    return fries_picked,cost,words
#Iteration 4
def ketchup(cost, words):
    while True:
        input2 = input("How much \033[1;35mKetchup\033[1;0m do you want?\033[1;33m\n")
        if input2.isnumeric():
            input2 = int(input2)
            if input2 < 1000 and 0 < input2:
                cost += float(input2*0.25)
                words.append(f"\033[1;35mYou wanted: {input2} Ketchup packets\033[1;0m")
                break
            else:
                print("\033[1;31mError, Try inputing again! Make sure it is a number! & Less then 1,000!\033[1;0m")
        elif 0 == input2:
            words.append("\033[1;35mYou didn't want Ketchup packets\033[1;0m")
        else:
            print("\033[1;31mError, Try inputing again! Make sure it is a number! & Less then 1,000!\033[1;0m")
    return cost,words
while True:
    user_input = str.lower(input("Do you want a \033[1;32mSandwich (1)\033[1;0m, \033[1;36mDrink (2)\033[1;0m, \033[1;33mFrys (3)\033[1;0m, \033[1;35mKetchup (4)\033[1;0m, or are you \033[1;31mDone (5)\033[1;0m?\n"))
    if user_input == "1" or "s" in user_input and "f" not in user_input:
        sandwich_picked, cost, words = Sandwhich(words, cost)
    elif user_input == "2" or "dr" in user_input:
        drink_picked, cost, words = drinks(cost, words, sml)
    elif user_input == "3" or "f" in user_input:
        fries_picked, cost, words= frys(cost, words, sml)
    elif user_input == "4" or "k" in user_input:
        cost, words = ketchup(cost, words)
        if sandwich_picked == 0 and drink_picked == 0 and fries_picked == 0:
            word = ""
    elif user_input == "5" or "do" in user_input:
        if cost > 0:
            break
        else:
            user_input = str.lower(input("Are you sure you want to leave without ordering anything? \033[1;33my\033[1;0m, \033[1;31mn\033[1;0m \n"))
            if "y" in user_input:
                word = "\033[1;33mYou didn't want anything."
                break
            elif "n" not in user_input:
                print("\033[1;31mIncorect input\033[1;0m please put a \033[1;33mYes\033[1;0m or \033[1;31mNo\033[1;0m.")
    costs = "{:.2f}".format(cost)
    print(f"\033[1;0mYour current total is, ${costs}.")
for w in words:
    word += w
    index2 += 1
    if len(words)-1 == index2:
        index2 = len(words)+1
        if sandwich_picked != 0 or drink_picked != 0 or fries_picked != 0:
            word += ", and a "
        else:
            word += ", and "
    if len(words)-1 > index2:
        word += ", "
    elif len(words)+2 == index2:
        word += "!"
print(word)
if sandwich_picked > 0 and drink_picked > 0 and fries_picked > 0:
    cost -= 1
    print("\033[1;31mDiscounted!\033[1;0m")
costs = "{:.2f}".format(cost)
print(f"Your total cost is, ${costs}.")