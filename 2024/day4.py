# part 1: this counts all occurences of "xmas" in the word search vertically, horizontally, diagonally, and inversely
def findXmas(wordsearch):
    return searchRow(wordsearch, "XMAS") + searchCol(wordsearch, "XMAS") + searchDiag(wordsearch, "XMAS")

def searchRow(wordsearch, target):
    matches = 0
    length = len(target)
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[0])-3):
            if ''.join(wordsearch[i][j:j+length]) == target or ''.join(wordsearch[i][j:j+length]) == target[::-1]:
                matches += 1
    return matches

def searchCol(wordsearch, target):
    matches = 0
    for j in range(len(wordsearch[0])):
        for i in range(len(wordsearch)-3):
            col = ""
            for k in range(4):
                col += wordsearch[i+k][j]
            if col == target or col == target[::-1]:
                matches += 1
    return matches

def searchDiag(wordsearch, target):
    matches = 0
    for i in range(len(wordsearch)-3):
        for j in range(len(wordsearch[0])-3):
            diag1 = ""
            diag2 = ""
            y = 3
            for z in range(4):
                diag1 += wordsearch[i+z][j+z]
                diag2 += wordsearch[i+z][j+y]
                y -= 1
            if diag1 == target or diag1 == target[::-1]:
                matches += 1
            if diag2 == target or diag2 == target[::-1]:
                matches += 1
    return matches

# part 2: this counts all occurences of "mas" in the shape of an x
def findMas(wordsearch):
    matches = 0
    for i in range(len(wordsearch)-2):
        for j in range(len(wordsearch[0])-2):
            diag1 = ""
            diag2 = ""
            y = 2
            for z in range(3):
                diag1 += wordsearch[i+z][j+z]
                diag2 += wordsearch[i+z][j+y]
                y -= 1
            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                matches += 1
    return matches

if __name__ == "__main__":
    filename = input("Enter the file path to your crossword puzzle sheet here: \n")
    with open(filename, 'r') as file:
        sheet = file.read().split("\n")

    for i in range(len(sheet)):
        sheet[i] = list(sheet[i])

    print(f"XMAS matches: {findXmas(sheet)}\nX-MAS matches: {findMas(sheet)}\n* Merry Christmas! *")


