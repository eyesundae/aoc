#Advent of Code
#Day 1: Calorie Counting

def main():
	maxCalories= 0
	for x in open("AoC1.txt").read().split("\n\n"):
		maxCalories= max(maxCalories, (sum(list(map(int, x.split())))))
			
	print("Max calories: ", maxCalories)
	
if __name__ == "__main__":
	main()
