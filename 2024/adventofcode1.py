# part 1: this finds the distance between the pairs of minimum numbers gotten from each row
def getDistance(array):
    distance = 0
    array[0].sort()
    array[1].sort()
    for i in range(len(array[0])):
        distance += abs(int(array[0][i]) - int(array[1][i]))
    return distance

# part 2: this sums the products of the first row's values and their number of occurrences in the second row
def getSimilarity(array):
    score = 0
    for i in range(len(array[0])):
        score += int(array[0][i]) * array[1].count(array[0][i])

    return score

if __name__ == "__main__":
    filename = input("Type the file path to the historian list: \n")
    with open(filename, 'r') as file:
        list = file.read()
    
    listPairs = list.split()
    cols = len(listPairs)//2
    array = [[0] * cols for i in range(2)]

    i = 0
    for j in range(0, len(listPairs), 2):
        array[0][i] = listPairs[j]
        array[1][i] = listPairs[j+1]
        i += 1
    print(f"Total distance: {getDistance(array)}\nSimilarity score: {getSimilarity(array)}\n* Merry Christmas! *\n")
