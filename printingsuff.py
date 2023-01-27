import random

strategy_name = "paper then random"

def beat_move(move):
	if (move=="r"):
		return "p"
	if (move == "p"):
		return "s"
	if (move=="s"):
		return "r"

def move(my_history, their_history):
    if len(their_history) != 0:
        pick = random.choice(["r", "p", "s"])
        return pick
    elif (their_history[-1] == their_history[-2]):
        return beat_move(their_history[-1])
    else:
        return "p"