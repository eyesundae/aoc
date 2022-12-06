#Advent of Code
#Day 5: Supply Stacks
from fileinput import input
from pprint import pprint
import re
import time

floorMap, crates, doMove = [], [], []
working = 0

def flipOrientation(crates):
	return (list(map(list,zip(*crates))))

#truncate and remove empty spaces
def fixCargo (cargo):
	for x in cargo:
		for y in x:
			if not re.search('[a-zA-Z]', y):
				x.remove(y)

def cm9000(x):
	print("WORKING", x.strip())
	if len(x.strip()) > 1:
		doMove = re.findall(r'\d+', x.strip())
		#print("doMove", doMove)
		for nummer in range(int(doMove[0])):
			temp = crates[int(doMove[1]) - 1].pop()
			crates[int(doMove[2]) - 1].append(temp)

def cm9001(x):
	print("WORKING", x.strip())
	if len(x.strip()) > 1:
		doMove = re.findall(r'\d+', x.strip())
		#print("doMove", doMove)
		#difference from PART 1 here
		temp = len(crates[int(doMove[1]) - 1]) - int(doMove[0]) 
		for nummer in range(int(doMove[0])):
			#pop moving list
			crates[int(doMove[2]) - 1].append\
			(crates[int(doMove[1] ) - 1].pop(temp))

for x in input():
	if x == "\n":
		working = 1
		#lol put that here
		fixCargo(crates)
		fixCargo(crates)
		fixCargo(crates)
		
	if not working:
		#parse crates
		print("NOT WORKING\n", x.strip())
		cargoStack = []
		searchValue = 1
		while searchValue < len(x):
			cargoStack.append(x[searchValue])
			searchValue += 4
		cargoStack.reverse()
		floorMap.append(cargoStack)
		crates = flipOrientation(floorMap)
		crates.reverse()
		for z in crates:
			z.reverse()
		
	else:
		#move crates
		#PART 1
		cm9000(x)

		#PART 2
		#cm9001(x)

		pprint(crates)
		print("\n")
		#time.sleep(1)
			
