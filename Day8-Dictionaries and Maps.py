
if __name__ == '__main__':
    d = {}
    n = int(input().strip())
    
    # Read n phone book entries
    for i in range(n):
        line = input().strip().split()
        name = line[0]
        phone = line[1]
        d[name] = phone
    
    # Process queries
    while True:
        try:
            query = input().strip()
            if query in d:
                print(f"{query}={d[query]}")
            else:
                print("Not found")
        except EOFError:
            break
        