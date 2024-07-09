import sys

count = int(input())
for i in range(count):
    a , b = map(int, sys.stdin.readline().split())

    if a>b:
        l = a
        s = b
    else:
        l = b
        s = a

    while s != 0:
        r = l % s
        l = s
        s = r
        
    gcd = l
    lcd = int(a*b/gcd)
    print(lcd)

    