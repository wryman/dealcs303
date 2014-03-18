# File: Deal.py

# Description: 

# Student Name: William Ryman

# Student UT EID: wrr368

# Course Name: CS 303E

# Unique Number: 53465

# Date Created: 3/17/14

# Date Last Modified:

def main():
	#import random functions and initialize variables
	import random
	times=int(input("Enter number of times you want to play:"))
	switch_win=0
	i=0
	#print headers for columns using the r.just (right justified command)
	print(str("Prize").rjust(2),str("Guess").rjust(4),str("View").rjust(6),str("New Guess").rjust(8))
	#initialize loop to play game and switch answer
	while (i<times):
		prize_door=random.randint(1,3)
		guess=random.randint(1,3)
		view=1
		newguess=1
		while (view==prize_door or view==guess):
			view=random.randint(1,3)
		while (newguess==guess or newguess==view):
			newguess=random.randint(1,3)
		if prize_door==newguess:
			switch_win+=1
			#calculate win probability
		switch_probability=switch_win/times
		no_switch_probability=1-switch_probability
		i+=1
		print(repr(prize_door).rjust(2),"  ",repr(guess).rjust(4),repr(view).rjust(6),repr(newguess).rjust(8))
	print("Probability of winning if you switch=", round(switch_probability,2))
	print("Probability of winning if you do not switch=", round(no_switch_probability,2))
main()