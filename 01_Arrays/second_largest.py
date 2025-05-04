from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(nums):
    # Write your code here.
    if len(set(nums))< 2:
        return -1
    largest = second_largest = float('-inf')
    for num in nums:
        if num>largest:
            second_largest = largest
            largest = num
        elif num>second_largest and num!=largest:
            second_largest = num
    return second_largest if second_largest!=float('-inf') else -1




nums = [12, 1, 35, 10, 34, 1]
print(findSecondLargest(nums))