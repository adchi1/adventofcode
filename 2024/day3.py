import re
# part 1: this takes input data, scans for multiplication operations, and returns its product
def multiply(data):
    sum = 0
    pattern = re.compile(r'mul\([0-9]+,[0-9]+\)')
    operations = re.findall(pattern, data)
    for op in operations:
        op = op[4:].strip(")")
        operands = op.split(",")
        sum += int(operands[0])*int(operands[1])
    return sum

# part 2: this executes operations that haven't been disabled
def multEnabled(data):
    sum = 0
    operations = re.split('(do\(\)|don\'t\(\))', data)
    i = 0
    while i < len(operations)-1:
        if operations[i] == "do()":
            sum += multiply(operations[i+1])
            i += 1
        elif operations[i] == "don't()":
            i += 1
        else: 
            sum += multiply(operations[i])
        i += 1
    return sum

if __name__=="__main__":
    filepath = input("Type the file path to the corrupted data: \n")
    with open(filepath, 'r') as file:
        data = file.read()
    print(f"Multiplication results: {multiply(data)}\nEnabled multiplication results: {multEnabled(data)}\n* Merry Christmas *\n")
