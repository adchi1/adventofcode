# part 1: this counts the unique positions the guard will be on the map before leaving the map
# source: https://github.com/Goldenlion5648/AdventOfCode2024/blob/master/6.py
def countPositions(map, origin):
    pos = origin[:]
    positions = set()
    direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    dir = 0
    while (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[0])):
        positions.add((pos[0], pos[1]))
        if not (0 <= pos[0]+direction[dir][0] < len(map)) and (0 <= pos[1]+direction[dir][1] < len(map[0])):
            break
        while map[pos[0]+direction[dir][0]][pos[1]+direction[dir][1]] == "#":
            dir += 1
            dir %= 4
        pos[0] += direction[dir][0]
        pos[1] += direction[dir][1]
    return len(positions)

# part 2: this counts the unique positions one obstacle can be placed to trap a guard in a loop
# idea source: https://www.reddit.com/r/adventofcode/comments/1h7tovg/comment/m0nym3a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# i check if a loop occurs if the guard encounters the same barrier facing the same direction twice
def countObstacles(map, origin):
    # first we get all the guard's possible positions
    pos = origin[:]
    positions = []
    obstacles = set()
    row = len(map)
    col = len(map[0])
    direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    dir = 0
    while (0 <= pos[0] < row) and (0 <= pos[1] < col):
        positions.append(pos[:])
        if not (0 <= pos[0]+direction[dir][0] < row) and (0 <= pos[1]+direction[dir][1] < col):
            break
        while map[pos[0]+direction[dir][0]][pos[1]+direction[dir][1]] == "#":
            dir += 1
            dir %= 4
        pos[0] += direction[dir][0]
        pos[1] += direction[dir][1]
    
    for i in range(len(positions)):
        if positions[i][:] == positions[0][:]:
            continue
        else: 
            pos = positions[0][:]
            map[positions[i][0]][positions[i][1]] = "0"
            dir = 0
            bumps = set()
            while True:
                if not ((0 <= pos[0]+direction[dir][0] < row) and (0 <= pos[1]+direction[dir][1] < col)):
                    break
                while map[pos[0]+direction[dir][0]][pos[1]+direction[dir][1]] in ["#", "0"]:
                    if (pos[0], pos[1], dir) in bumps:
                        obstacles.add((positions[i][0], positions[i][1]))
                        break
                    bumps.add((pos[0], pos[1], dir))
                    dir += 1
                    dir %= 4
                pos[0] += direction[dir][0]
                pos[1] += direction[dir][1]
            map[positions[i][0]][positions[i][1]] = "."
    return len(obstacles)

if __name__ == "__main__":
    filename = input("Enter the file path to the map: \n")
    with open(filename, 'r') as file:
        map = [list(m) for m in file.read().split("\n")]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                origin = [i, j]
                break
    print(f"Distinct positions: {countPositions(map, origin)}")
    print(f"Possible obstacles: {countObstacles(map, origin)}")
    print(f"* Merry Christmas! *")