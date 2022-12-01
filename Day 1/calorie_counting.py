import pathlib

# Part 1
calories = pathlib.Path("input.txt").read_text()
calories_per_elf = [sum(map(int, elf.split("\n"))) for elf in calories.split("\n\n")]

print(max(calories_per_elf))
