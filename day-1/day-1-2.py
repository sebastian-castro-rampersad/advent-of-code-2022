with open('input.txt') as input:
    line = input.readline()
    top_three = [0] * 3
    actual_calories = 0

    while line:
        if line == '\n' and actual_calories > top_three[2]:
            if actual_calories > top_three[2] and actual_calories < top_three[1]:
                top_three[2] = actual_calories
            elif actual_calories > top_three[1] and actual_calories < top_three[0]:
                top_three[2] = top_three[1]
                top_three[1] = actual_calories
            elif actual_calories > top_three[0]:
                top_three[2] = top_three[1]
                top_three[1] = top_three[0]
                top_three[0] = actual_calories
            actual_calories = 0
        elif line == '\n':
            actual_calories = 0
        else:
            actual_calories += int(line)
        line = input.readline()

print(sum(top_three))
