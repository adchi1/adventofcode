# part 1: this returns the sum of the medians of each update that follows all the provided rules
def isCorrect(rules, update):
    for i in range(len(update)):
        try:
            successors = rules[update[i]]
        except:
            successors = set()
        predecessors = set()
        for key in list(rules.keys()):
            if update[i] in rules[key]:
                predecessors.add(key)
        if any(num in successors for num in update[:i]) or any(num in predecessors for num in update[i+1:]):
            return False
    return True 

def sumUpdates(rules, updates):
    validUpdates = []
    for update in updates:
        if isCorrect(rules, update):
            validUpdates.append(update)
    return sum([int(update[len(update)//2]) for update in validUpdates])

# part 2: this returns the sum of medians of each incorrect update that has been altered to follow the rules
def sumFixUpdates(rules, updates):
    fixedUpdates = []
    #source: https://github.com/RD-Dev-29/advent_of_code_24/blob/main/code_files/day5.py
    for update in updates:
        if not isCorrect(rules, update):
            for j in range(len(update)):
                for k in range(j+1, len(update)):
                    try:
                        value = rules[update[k]]
                    except:
                        value = set()
                    if update[j] in value:
                        update[j], update[k] = update[k], update[j]
            fixedUpdates.append(update)
    return sum([int(update[len(update)//2]) for update in fixedUpdates])

def convertRules(rules):
    keys = []
    values = []
    for i in range(len(rules)):
        keys.append(rules[i][0])
        value = set()
        for j in range(len(rules)):
            if rules[i][0] == rules[j][0]:
                value.add(rules[j][1])
        values.append(value)
    return dict(zip(keys, values))

if __name__ == "__main__":
    filename = input("Enter the file path to the rules and updates: \n")
    with open(filename, 'r') as file:
        info = file.read().split("\n\n")
    rules = info[0].split("\n")
    for i in range(len(rules)):
        rules[i] = rules[i].split("|")
    rules = convertRules(rules)

    updates = info[1].split("\n")
    for i in range(len(updates)):
        updates[i] = updates[i].split(",")

    print(f"Part 1: {sumUpdates(rules, updates)}")
    print(f"Part 2: {sumFixUpdates(rules, updates)}")
    print(f"* Merry Christmas! *")

    

        

