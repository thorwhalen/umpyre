

# https://adventofcode.com/2020/day/1

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


               
           
