#Advent of Code
#Day 2: Rock Paper  Scissors
from fileinput import input

shapes = ["A", "B", "C"]
otherShapes = ["X", "Y", "Z"]

rpcKey = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
keyTwo = [[3, 1, 2], [4, 5, 6], [8, 9, 7]]

score, scoreTwo = 0, 0

for x in input():
	if x is None:
		break
	rpc = x.split()
	score += (rpcKey[shapes.index(rpc[0])][otherShapes.index(rpc[1])])
  
  #something flipped?
	scoreTwo += (keyTwo[otherShapes.index(rpc[1])][shapes.index(rpc[0])])
	#(keyTwo[shapes.index(rpc[0])][otherShapes.index(rpc[1])])

print("PartOne: ", score)
print("PartTwo: ", scoreTwo)
