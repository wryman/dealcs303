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
		while (view==prize_door or view==guess):
			view=random.randint(1,3)
		print("pd",prize_door)
		print("g",guess)
		print("v",view)
		i+=1
main()