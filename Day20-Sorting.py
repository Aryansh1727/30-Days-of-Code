
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps = 0
    for i in range(n):
        Swapped = False
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                numSwaps += 1 
                Swapped=True
        if not Swapped:
            break
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}") 
    print(f"Last Element: {a[-1]}")  
            
            
            
            