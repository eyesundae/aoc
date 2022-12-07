#Advent of Code
#Day 6: Tuning Trouble
from fileinput import input

comms= []
pos = 0

def isUnique(piece):
	checked = ""
	for a in piece:
		if a in checked:
			return False
		checked += a
	return True

#weird formatting
q = list(input())
r = str(q)
sentence = r.strip("[']")

#need to check for comm of length 14
for x in sentence:
	#print("character: ", x, end="\n")
	if len(comms) < 4: #14
		comms.append(x)
		pos += 1
	else:
		print(comms, end="\n")
		if not isUnique(comms):
			comms.pop(0)
			comms.append(x)
			pos += 1
		else:
			print("\n\nstring: ", comms, "\npos:", pos, "\n")
			#answer.append(comms)
			#answer.append(pos)
			break
			
