#!/usr/bin/env python
# coding: utf-8

import numpy as np

def read_file_as_char_array(filename):
    """Reads a text file into a 2D NumPy array of single characters."""

    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())

    # Create a 2D array of the appropriate size
    char_array = np.full((len(lines), len(lines[0])), ' ')

    # Fill the array with characters
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            char_array[i, j] = char

    return char_array

def get_xmas_vectors(arr, index):
    nrows, ncols = arr.shape
    # Form a list of vectors for directions N, NE, E, SE, S, SW, W, NW
    vec_list = [None] * 8
    # N
    if index[0] >= 3:
        vec_list[0] = np.flip(arr[index[0]-3:index[0]+1, index[1]])
    # NE
    if index[0] >= 3 and index[1] < ncols - 3:
        vec_list[1] = np.diag(np.flipud(arr[index[0]-3:index[0]+1, index[1]:index[1]+4]))
    # E
    if index[1] < ncols - 3:
        vec_list[2] = arr[index[0], index[1]:index[1]+4]
    # SE
    if index[0] < nrows - 3 and index[1] < ncols - 3:
        vec_list[3] = np.diag(arr[index[0]:index[0]+4, index[1]:index[1]+4])
    # S
    if index[0] < nrows - 3:
        vec_list[4] = arr[index[0]:index[0]+4, index[1]]
    # SW
    if index[0] < nrows - 3 and index[1] >= 3:
        vec_list[5] = np.diag(np.fliplr(arr[index[0]:index[0]+4, index[1]-3:index[1]+1]))
    # W
    if index[1] >= 3:
        vec_list[6] = np.flip(arr[index[0], index[1]-3:index[1]+1])
    # NW
    if index[0] >= 3 and index [1] >= 3:
        vec_list[7] = np.flip(np.diag(arr[index[0] - 3 : index[0] + 1, index[1] - 3: index[1] + 1]))
    
    return vec_list

def get_mas_xvectors(arr, index):
    vec_list = [None] * 2
    vec_list[0] = np.asarray([arr[index[0]-1, index[1]-1], arr[index[0], index[1]], arr[index[0]+1, index[1]+1]])
    vec_list[1] = np.asarray([arr[index[0]+1, index[1]-1], arr[index[0], index[1]], arr[index[0]-1, index[1]+1]])

    return vec_list
    
# Read char array
chars = read_file_as_char_array('data/dec04-1.txt')
print(chars)

nrows, ncols = chars.shape
xmas_counter = 0
for index in np.ndindex(chars.shape):
    if chars[index] == 'X':
        xmas_vectors = get_xmas_vectors(chars, index)
        #print(xmas_vectors)
        for vec in xmas_vectors:
            if vec is not None:
                #print(vec)
                if np.array_equal(vec, np.asarray(['X', 'M', 'A', 'S'])):
                    xmas_counter += 1
print('xmas count:', xmas_counter)

# Part 2
mas_counter = 0
for i in range(1, nrows-1):
    for j in range(1, ncols-1):
        if chars[i, j] == 'A':
            mas_vectors = get_mas_xvectors(chars, (i, j))
            if (np.array_equal(mas_vectors[0], np.asarray(['M', 'A', 'S'])) or np.array_equal(mas_vectors[0], np.asarray(['S', 'A', 'M']))) and \
               (np.array_equal(mas_vectors[1], np.asarray(['M', 'A', 'S'])) or np.array_equal(mas_vectors[1], np.asarray(['S', 'A', 'M']))):
                mas_counter += 1
print('x-mas count:', mas_counter)
