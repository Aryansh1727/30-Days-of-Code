# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(n):
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


T = int(input())

for _ in range(T):
    n = int(input())

    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")