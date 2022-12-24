RANKING_SIZE = 3

def insert_in_ranking(ranking, actual_calories):
    for i in reversed(range(len(ranking))):
        if i == 0 and actual_calories > ranking[i]:
            return [actual_calories] + ranking[:-1]
        elif actual_calories > ranking[i] and actual_calories < ranking[i-1]:
            return ranking[:i] + [actual_calories] + ranking[i:-1]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

with open('input.txt') as input:
    line = input.readline()
    ranking = [0] * RANKING_SIZE
    actual_calories = 0

    while line:
        if line == '\n' and actual_calories > ranking[RANKING_SIZE-1]:
            ranking = insert_in_ranking(ranking, actual_calories)
            actual_calories = 0
        elif line == '\n':
            actual_calories = 0
        else:
            actual_calories += int(line)
        line = input.readline()

print(sum(ranking))
