# Part 1
with open("input.txt") as file:
    calories = file.read()
calories_per_elf = [sum(map(int, elf.split("\n"))) for elf in calories.split("\n\n")]

print(max(calories_per_elf))

# Part 2
print(sum(sorted(calories_per_elf, reverse=True)[:3]))
