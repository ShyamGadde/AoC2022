from string import ascii_letters

priority = {ch: i + 1 for i, ch in enumerate(ascii_letters)}

with open("input.txt") as file:
    rucksacks = [line.strip() for line in file]

# Part 1
priority_sum = sum(priority[str(*set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:]))]
                   for rucksack in rucksacks)
print(priority_sum)


# Part 2
groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

priority_sum1 = sum(priority[str(*set(group[0]).intersection(group[1], group[2]))] for group in groups)
print(priority_sum1)
