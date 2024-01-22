def count_food(days):
    sm = 0
    for day in days:
        sm += daily_food[day - 1]
    return sm

daily_food = [0, 150, 150]
print(count_food([2, 3]))