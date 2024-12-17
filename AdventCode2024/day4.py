import numpy as np
import re
from utils import read_str_file

def main():
    """Day 4: Ceres Search.

    A small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search.
    She only has to find one word: XMAS.
    This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them.
    Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....

    """
    word_search = read_str_file('input4.txt')

    day4_part1(word_search)
    day4_part2(word_search)
    

def list_wordsearch(total_xmas, list_wordsearch):
    for line in list_wordsearch:
        # To handle overlapping the words: ?=
        horizontal = re.findall(r"(?=(XMAS|SAMX))", line)
        total_xmas += len(horizontal)
    return total_xmas

def extract_diagonals(grid):
    rows, cols = grid.shape
    diagonals = []

    # Top-left to bottom-right diagonals
    # grid.diagonal: Extracts the k-th diagonal.
    # k=0 gives the main diagonal, k>0 gives diagonals above the main, and k<0 gives diagonals below the main.
    for k in range(-rows + 1, cols):
        diagonals.append(''.join(grid.diagonal(k)))
    
    # Top-right to bottom-left diagonals
    flipped_grid = np.fliplr(grid)
    for k in range(-rows + 1, cols):
        diagonals.append(''.join(flipped_grid.diagonal(k)))

    return diagonals

def day4_part1(word_search):
    """How many times does XMAS appear?
    """
    total_xmas = 0

    # Horizontal Search
    total_xmas = list_wordsearch(total_xmas, word_search)

    # Convert to 2D NumPy array of characters
    array_wordsearch = np.array([list(line) for line in word_search])

    # Vertical Search
    transposed_array_wordsearch = np.transpose(array_wordsearch)
    vertical_wordsearch = []
    for line in transposed_array_wordsearch:
        vertical_wordsearch.append("".join(line))
    total_xmas = list_wordsearch(total_xmas, vertical_wordsearch)

    # Diagonal Search
    diagonals = extract_diagonals(array_wordsearch)
    total_xmas = list_wordsearch(total_xmas, diagonals)

    print("Total times XMAS shows up in word_search:", total_xmas)
        

def day4_part2(word_search):
    """It's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
     
    One way to achieve that is like this:
        M.S
        .A.
        M.S
    """
    # Convert to 2D NumPy array of characters
    array_wordsearch = np.array([list(line) for line in word_search])

    total_x_mas = 0
    result = np.where(array_wordsearch == 'A')
    for row, col in zip(result[0], result[1]):
        if (row == len(word_search) - 1) or (col == len(word_search) - 1):
            continue

        # Extract diagonal values for readability
        upper_left = array_wordsearch[row-1, col-1]
        lower_right = array_wordsearch[row+1, col+1]
        lower_left = array_wordsearch[row+1, col-1]
        upper_right = array_wordsearch[row-1, col+1]

        # Define conditions for diagonals
        left_diagonal_condition = (upper_left == "M" and lower_right == "S") or (upper_left == "S" and lower_right == "M")
        right_diagonal_condition  = (lower_left == "M" and upper_right == "S") or (lower_left == "S" and upper_right == "M")

        # Check all diagonal conditions
        if left_diagonal_condition and right_diagonal_condition:
            total_x_mas += 1

    print("Total times X-MAS shows up in word_search:", total_x_mas)


if __name__ == '__main__':
    main()
