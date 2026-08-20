import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    hourglass_sum = 0
    i, j = 0, 0
    
    while i != 3 or j != 4:
        if j == 4:
            j = 0
            i += 1
        
        hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
        if i == 0 and j == 0:
            max_sum = hourglass_sum
        else:
            max_sum = max(hourglass_sum, max_sum)
        
        j += 1
    
    print(max_sum)