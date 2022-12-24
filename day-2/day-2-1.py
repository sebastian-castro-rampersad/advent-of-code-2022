with open('input.txt') as input:
    line = input.readline()
    # X -> Rock | Y -> Paper | Z -> Scissors
    points_by_movment = {'X': 1, 'Y': 2, 'Z': 3}
    combinations = {'X': {'A': 3, 'B': 0, 'C': 6},
                    'Y': {'A': 6, 'B': 3, 'C': 0},
                    'Z': {'A': 0, 'B': 6, 'C': 3}}
    score = 0

    while line:
        game = line.split()
        score += points_by_movment[game[1]] + combinations[game[1]][game[0]]
        line = input.readline()

print(score)
