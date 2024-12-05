#!/usr/bin/env python
# coding: utf-8

def check_safe(diffs):
    if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]):
        return 1
    else:
        return 0

# Open data file and read it into two columns
filename = "data/dec02-1.txt"
levels_list = []
diffs_list = []
safe_diffs_count = 0
repairable_diffs_count = 0
with open(filename, 'r') as file:
    for line in file:
        # Split the line into values (assuming space-separated)
        values = line.split()
        levels = [int(value) for value in values]
        levels_list.append(levels)
        # Calculate diffs between values
        diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
        diffs_list.append(diffs)

# Check if diffs are within bounds
for i, diffs in enumerate(diffs_list):
    #if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]): 
    if check_safe(diffs) == 1:
        safe_diffs_count += 1
    else:
        # Defect counters
        num_neg = sum(1 for diff in diffs if diff < 0)
        num_zero = diffs.count(0)
        num_pos = sum(1 for diff in diffs if diff > 0)
        num_hi = sum(1 for diff in diffs if diff >= 4)
        num_lo = sum(1 for diff in diffs if diff <= -4)
        levels = levels_list[i].copy()
        if num_zero + num_hi + num_lo <= 1:
            if num_zero == 1:
                del levels[diffs.index(0)+1]
                diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                if check_safe(diffs) == 1: 
                    repairable_diffs_count += 1
            elif num_neg == 1: # single neg number
                idx = [i for i in range(len(diffs)) if diffs[i] < 0][0]
                del levels[idx]
                diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                if check_safe(diffs) == 1: 
                    repairable_diffs_count += 1
                else:
                    levels = levels_list[i].copy()
                    del levels[idx + 1]
                    diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                    if check_safe(diffs) == 1: 
                        repairable_diffs_count += 1
            elif num_pos == 1: # single pos number
                idx = [i for i in range(len(diffs)) if diffs[i] > 0][0]
                del levels[idx]
                diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                if check_safe(diffs) == 1: 
                    repairable_diffs_count += 1
                else:
                    levels = levels_list[i].copy()
                    del levels[idx + 1]
                    diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                    if check_safe(diffs) == 1: 
                        repairable_diffs_count += 1
            elif num_lo == 1: # single number with diff < -3
                idx = [i for i in range(len(diffs)) if diffs[i] < -3][0]
                del levels[idx]
                diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                if check_safe(diffs) == 1: 
                    repairable_diffs_count += 1
                else:
                    levels = levels_list[i].copy()
                    del levels[idx + 1]
                    diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                    if check_safe(diffs) == 1: 
                        repairable_diffs_count += 1
            elif num_hi == 1: # single number with 
                idx = [i for i in range(len(diffs)) if diffs[i] > 3][0]
                del levels[idx]
                diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                if check_safe(diffs) == 1: 
                    repairable_diffs_count += 1
                else:
                    levels = levels_list[i].copy()
                    del levels[idx + 1]
                    diffs = [y - x for x, y in zip(levels[:-1], levels[1:])]
                    if check_safe(diffs) == 1: 
                        repairable_diffs_count += 1

print("Number of safe reports:", safe_diffs_count)
print("Number of repairable reports:", repairable_diffs_count)
print("Total safe and repairable reports:", safe_diffs_count + repairable_diffs_count)

