import numpy as np

def file_parser(input_file):
    # Also possible to just split on new line and sum elements.
    # But this keeps track of what elf carries what.

    elf_dict = {}
    elf_counter, elf_calorie = 0, 0

    for line in input_file:
        if len(line.strip()) == 0:
            elf_counter += 1
            elf_calorie = 0
        else:
            elf_calorie += int(line)
        elf_dict[elf_counter] = elf_calorie

    return elf_dict


with open('C:\\code\\aoc2022\\01-12\\input.txt', 'r') as file:
    elf_dict = file_parser(file)
    print("Largest calorie count: ", max(elf_dict.values()))

    calorie_list = list(elf_dict.values())
    print(sum(sorted(calorie_list)[-3:]))