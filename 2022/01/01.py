#Advent of Code
#Day 1: Calorie Counting

def main():
	elves = []
	for x in open("AoC1.txt").read().split("\n\n"):
		thisElf = (sum(list(map(int, x.split()))))
		elves.append(thisElf)

	print("Fatty ELF number ", 	elves.index(max(elves))+1, 
	", they've got ", max(elves), " calories!")
	
if __name__ == "__main__":
	main()

