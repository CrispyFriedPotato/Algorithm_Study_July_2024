f_a1, f_a0 = map(int,input().split())

c = int(input())
n0 = int(input())

valid = 1
for i in range(n0,101):
    if f_a1*i + f_a0 <= c*i:
        pass
    else:
        valid = 0
        break
print(valid)
