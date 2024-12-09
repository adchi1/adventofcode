# part 1: this returns 1 if the report has all ascending or descending values and don't have drastic value differences, and 0 otherwise
def isSafe(report):
    ascending = True
    descending = True
    jumping = False
    for i in range(len(report)-1):
        num1 = int(report[i])
        num2 = int(report[i+1])
        if num1 < num2:
            descending = False
        if num1 > num2:
            ascending = False
        if not abs(num1 - num2) in [1,2,3]:
            jumping = True
    if (not jumping) and (ascending or descending):
        return 1
    return 0

# part 2: this returns 1 if the report is safe after removing a level, and 0 otherwise
def isDampened(report):
    if isSafe(report) == 1:
        return 1
    else:
        for i in range(len(report)):
            copy = report[:i] + report[i+1:]
            print(copy)
            if isSafe(copy) == 1:
                return 1
        return 0

if __name__ == "__main__":
    filename = input("Type the file path to the reports: \n")
    with open(filename, 'r') as file:
        reports = file.read().split("\n")
    for i in range(len(reports)):
        reports[i] = reports[i].split()
    
    print(f"Safe reports: {sum([isSafe(report) for report in reports])}")
    print(f"Safe reports after dampening: {sum([isDampened(report) for report in reports])}") 
    print(f"* Merry Christmas! *")