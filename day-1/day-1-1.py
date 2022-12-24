with open('input-1.txt') as input:
    line = input.readline()
    most_calories = 0
    actual_calories = 0

    while line:
        if line == '\n' and actual_calories > most_calories:
            most_calories = actual_calories
            actual_calories = 0
        elif line == '\n':
            actual_calories = 0
        else:
            actual_calories += int(line)
        line = input.readline()

print(most_calories)
