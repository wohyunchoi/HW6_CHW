import random
import csv

def RandomDice():
    RandomList = []
    number = int(input("시행 횟수:"))
    for i in range(number):
        RandomNum = random.randint(1,6)
        RandomList.append(RandomNum)
        numberS = str(number)

        with open('random'+numberS+'.csv','w', newline='') as csvfile:
            numwriter = csv.writer(csvfile, delimiter='\n')
            numwriter.writerow(RandomList)

if __name__ == "__main__":
    RandomDice()
