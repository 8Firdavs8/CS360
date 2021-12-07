import sys
n, m = map(int, sys.stdin.readline().split())
while n + m > 0:
    x = set()
    for _ in range(n):
        x.add(int(sys.stdin.readline()))

    counter = 0
    for _ in range(m):
        if int(sys.stdin.readline()) in x:
            counter += 1

    print(counter)

    n, m = map(int, sys.stdin.readline().split())
