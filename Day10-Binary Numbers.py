import math
import os
import random
import re
import sys


def decimal_to_binary_loop(n):
    if n == 0:
        return "0"
    
    binary_digits = []
    while n > 0:
        remainder = n % 2          
        binary_digits.append(str(remainder))
        n = n // 2         
        
    # Reverse the array since remainders are found from last to first
    return "".join(reversed(binary_digits))


def count_consecutive_ones(n):
    binary = bin(n)[2:]
    
    max_count = 0
    current_count = 0
    
    # Iterate through each bit
    for bit in binary:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count


if __name__ == '__main__':
    n = int(input().strip())
    result = count_consecutive_ones(n)
    print(result)