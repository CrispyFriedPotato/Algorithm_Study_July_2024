from sys import stdin

n = int(stdin.readline().strip())

expect = list(map(int,stdin.readlines()))

expect.sort()
real = [i for i in range(1,n+1)]
total = 0
for i in range(n):
     total += abs(expect[i]-real[i])

print(total)    