inputneeded = ["___________"]*15 #Setting a list for every input needed

def  rmadlib():
    global inputneeded #Getting the preveisly set list
	#The actual madlib text
    return [f"Pizza was invented by a {inputneeded[0]} [adjective]",
            f"{inputneeded[1]} [nationality]",
            f"chef named {inputneeded[2]} [person].",
            f"To Make a pizza, you need to take a lump of {inputneeded[3]} [noun],",
            f"and make a thin, round {inputneeded[4]} [adjective]",
            f"{inputneeded[5]} [noun].",
            f"Then you cover it with {inputneeded[6]} [adjective] sauce,",
            f"{inputneeded[7]} [adjective] cheese,",
            f"and fresh chpped {inputneeded[8]} [plural noun].",
            f"Next you have to bake it in a very {inputneeded[9]} [noun].",
            f"When it is done, cut it into {inputneeded[10]} [number],",
            f"{inputneeded[11]} [shape].",
            f"Some kids like {inputneeded[12]} [food] pizza the best,",
            f"but my favorite is the {inputneeded[13]} [food].",
            f"If I could, I would eat pizza {inputneeded[14]} [number] times a day!"]

def pmadlib():
    madlib = rmadlib() #Setting the madlib var to the madlib text
    for i in madlib:
        inputneeded[madlib.index(i)] = input(i + "\n") #Changing the inputneeded spot at the index that was printed and getting there input on what to change it to
    madlib = rmadlib() #Updating the madlib var so that it has the user inputs in it
    for i in madlib:
        print(i, end = " ")#printing the new msg with user input
    print("\n")

pmadlib() #Calling the fuction that does everything