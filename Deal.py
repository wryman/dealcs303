# File: Deal.py

# Description: 

# Student Name: William Ryman

# Student UT EID: wrr368

# Course Name: CS 303E

# Unique Number: 53465

# Date Created: 3/17/14

# Date Last Modified:

def main():
	import random
	times=int(input("Enter number of times you want to play:"))
	switch_win=0
	i=0
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
		switch_probability=switch_win/times
		no_switch_probability=1-switch_probability
		print("Prize",  "Guess",  "View",  "New Guess")
		print("prizedoor=",prize_door)
		print("guess=",guess)
		print("view=",view)
		print("new guess=",newguess)
		print("switch win=",switch_win)
		print("Probability of winning if you switch=", round(switch_probability,2))
		print("Probability of winning if you do not switch=", round(no_switch_probability,2))
		i+=1
main()