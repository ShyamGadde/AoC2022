with open("input.txt") as file:
    sections = [line.strip().split(",") for line in file]

# Part 1
overlaps = 0
intersections = 0
for section in sections:
    assignment1_str = list(map(int, section[0].split("-")))
    assignment2_str = list(map(int, section[1].split("-")))
    assignment1 = set(range(assignment1_str[0], assignment1_str[1] + 1))
    assignment2 = set(range(assignment2_str[0], assignment2_str[1] + 1))
    if assignment1.issubset(assignment2) or assignment2.issubset(assignment1):
        overlaps += 1
    if assignment1.intersection(assignment2):
        intersections += 1

print(overlaps)
print(intersections)
