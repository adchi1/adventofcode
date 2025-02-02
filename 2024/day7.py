import itertools

# this function returns the results of an equation by evaluating operands with one or more operators
def getResult(operands, operator):
    result = int(operands[0])
    for i in range(1, len(operands)):
        if operator[0] == '+':
            result += int(operands[i])
        elif operator[0] == '*':
            result *= int(operands[i])
        elif operator[0:2] == '||':
            result = int(str(result)+operands[i])
            operator = operator[1:]
        operator = operator[1:]
    return result

# this function returns the results of each equation 
def validResults(equations, signs):
    sum = 0
    for result in equations:
        num = len(equations[result])-1
        operators = [''.join(comb) for comb in itertools.product(signs, repeat=num)]
        for operator in operators:
            if getResult(equations[result], operator) == int(result):
                sum += result
                break
    return sum
    

if __name__ == "__main__":
    with open(input("Enter the file path to the equations: \n"), 'r') as file:
        equations = [equation.split(":") for equation in file.read().split("\n")]
    results = []
    operands = []
    for equation in equations:
        results.append(equation[0])
        operands.append(equation[1].split())
    equations = dict(zip(results, operands))

    print(f"First calibration result: {validResults(equations, ['+','*'])}")
    print(f"Second calibration result: {validResults(equations, ['+', '*', '||'])}")
    print("* Merry Christmas! *")