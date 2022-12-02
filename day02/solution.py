# Part 1
with open("input.txt") as file:
    rounds = [line.strip() for line in file]

choice = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

play = {
    ('A', 'X'): 3,
    ('B', 'X'): 0,
    ('C', 'X'): 6,
    ('A', 'Y'): 6,
    ('B', 'Y'): 3,
    ('C', 'Y'): 0,
    ('A', 'Z'): 0,
    ('B', 'Z'): 6,
    ('C', 'Z'): 3
}

score = 0
for rnd in rounds:
    opponent, me = rnd.split()
    score += play[(opponent, me)] + choice[me]

print(score)
