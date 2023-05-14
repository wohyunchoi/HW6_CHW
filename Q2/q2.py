import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":

    f100 = open('random100.csv')
    f1000 = open('random1000.csv')
    f10000 = open('random10000.csv')
    f100000 = open('random100000.csv')

    data100 = csv.reader(f100)
    data1000 = csv.reader(f1000)
    data10000 = csv.reader(f10000)
    data100000 = csv.reader(f100000)

    result100 = []
    result1000 = []
    result10000 = []
    result100000 = []

    for row in data100:
        if row[0] != '':
            result100.append(int(row[0]))

    for row in data1000:
        if row[0] != '':
            result1000.append(int(row[0]))

    for row in data10000:
        if row[0] != '':
            result10000.append(int(row[0]))

    for row in data100000:
        if row[0] != '':
            result100000.append(int(row[0]))

    f100.close()
    f1000.close()
    f10000.close()
    f100000.close()
    plt.title("Number of dice")
    plt.subplot(2,2,1)
    plt.hist(result100, bins = 200)
    plt.title('roll dice 100 times')
    plt.subplot(2,2,2)
    plt.hist(result1000, bins = 200)
    plt.title('roll dice 1000 times')
    plt.subplot(2,2,3)
    plt.hist(result10000, bins = 200)
    plt.title('roll dice 10000 times')
    plt.subplot(2,2,4)
    plt.hist(result100000, bins = 200)
    plt.title('roll dice 100000 times')
    plt.show()
    
