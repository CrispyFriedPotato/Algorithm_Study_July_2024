from sys import stdin

n = int(stdin.readline().strip())
p = list(map(int,stdin.readline().split()))
p.sort()
time = 0
for i in range(1,n+1):
    time += sum(p[0:i])
print(time)
