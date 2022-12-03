from string import ascii_letters

priority = {ch: i + 1 for i, ch in enumerate(ascii_letters)}

with open("input.txt") as file:
    rucksacks = [line.strip() for line in file]

# Part 1
priority_sum = sum(priority[str(*set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:]))]
                   for rucksack in rucksacks)
print(priority_sum)


