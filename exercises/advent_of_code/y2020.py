
######################################################################################################
# https://adventofcode.com/2020/day/1 ################################################################

from math import prod
from itertools import combinations

def report_repair(numbers, target=2020, tuple_size=2):
    """
    https://adventofcode.com/2020/day/1
    """
    return next(map(                              # get the first
        prod,                                     # product
        filter(lambda pair: sum(pair) == target,  # numbers that sum to target
               combinations(numbers, tuple_size))))           # from the "list" of all pairs of numbers
               
               
report_numbers = map(float, 
"""1721
979
366
299
675
1456""".split('\n'))

assert report_repair(report_numbers) == 514579


######################################################################################################
# https://adventofcode.com/2020/day/3 ################################################################

example_pattern = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

from itertools import cycle
from builtins import sum

def slide(pattern=example_pattern, right=3, down=1, output_func=lambda x: x == '#'):
    pattern_rows = pattern.split('\n')
    nrows = len(pattern_rows)
    ncols = len(pattern_rows[0])    
    row, col = down, right
    while row < nrows:
        yield output_func(pattern_rows[row][col % ncols])
        row += down
        col += right
        
        
assert sum(slide(example_pattern)) == 7

def multi_slides(pattern=example_pattern, 
                 right_down_pairs=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)],
                 output_func=lambda x: x == '#'):
    for right, down in right_down_pairs:
        yield sum(slide(pattern, right, down, output_func))
        
import math
assert math.prod(multi_slides()) == 336

           
