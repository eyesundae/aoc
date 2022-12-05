#Advent of Code
#Day 4: Camp Cleanup
from fileinput import input
import re

samePair = 0
overlapJobs = 0

for x in input():
	a, b = [], []
	basket = re.split("-|,", x.rstrip())
	a = set(range(int(basket[0]), int(basket[1] ) + 1))
	b = set(range(int(basket[2]), int(basket[3] ) + 1))
	
	if(a.intersection(b)):
		overlapJobs += 1
	if a.issubset(b) and not a.difference(b):
		samePair += 1
	elif a.issuperset(b) and not b.difference(a):
		samePair += 1
    
print("# pairs:", samePair)	
print("# overlapping jobs: ", overlapJobs)
