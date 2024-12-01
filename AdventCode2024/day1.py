import numpy as np
from utils import read_two_column_file

def main():
    """Day 1: Historian Hysteria.
    """
    loc_id1, loc_id2 = read_two_column_file('input1.txt')

    loc_id1.sort()
    loc_id2.sort()

    diff_ids = np.absolute(np.array(loc_id1) - np.array(loc_id2))

    print("Part1 - Distance ids", sum(diff_ids))

    similarity_score = 0

    for id in loc_id1:
        similarity_score += id * loc_id2.count(id)
    
    print("Part2 - Similarity Score", similarity_score)

if __name__ == '__main__':
    main()
