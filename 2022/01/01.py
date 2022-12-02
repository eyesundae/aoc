#Advent of Code
#Day 1: Calorie Counting

def main():
	elves = []
	for x in open("AoC1-2.txt").read().split("\n\n"):
		thisElf = (sum(list(map(int, x.split()))))
		elves.append(thisElf)

	print("Fatty ELF number ",  elves.index(max(elves))+1, 
	", they've got ", max(elves), " calories!")
	
	elves.sort(reverse=True)
	print("Top 3 elves carrying: ", 
	sum(elves[:3]), " calories")
	
if __name__ == "__main__":
	main()

