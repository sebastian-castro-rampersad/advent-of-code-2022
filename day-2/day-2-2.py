with open('input.txt') as input:
    line = input.readline()
    # X -> Lose | Y -> Draw | Z -> Win
    points_by_situation = {'X': 0, 'Y': 3, 'Z': 6}
    combinations = {'X': {'A': 3, 'B': 1, 'C': 2},
                    'Y': {'A': 1, 'B': 2, 'C': 3},
                    'Z': {'A': 2, 'B': 3, 'C': 1}}
    score = 0

    while line:
        game = line.split()
        score += points_by_situation[game[1]] + combinations[game[1]][game[0]]
        line = input.readline()

print(score)
