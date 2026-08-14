# even place start at 0 and odd place start at 1
def print_even(string: str):
    for i in range(0, len(string), 2):
        print(string[i], end="")
    
def print_odd(string: str):
    for i in range(1, len(string), 2):
        print(string[i], end="")

if __name__ == '__main__':
    N = int(input().strip())
    strings = []
    
    for _ in range(N):
        s = input().strip()
        strings.append(s)
        
    for string in strings:
        print_even(string)
        print(" ", end="")
        print_odd(string)
        print()
