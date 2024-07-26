from sys import stdin

n , k = map(int, stdin.readline().split())

people = [i for i in range(1,n+1)]
i=0 # idx
res = []
while len(people) !=0 :
    if i+(k-1) < len(people):
        res.append(str(people[i+(k-1)]))
        del people[i+(k-1)]
        if i == len(people)-(k-1):
            i=0
        else:
            i+=(k-1)
    else:
        i = (i+(k-1))%len(people)
        if len(people) == 1:
            res.append(people[i])
        else:
            res.append(people[i])
        del people[i]

for i,r in enumerate(res):
    if i ==0:
        print('<',end="")
    print(r,end="")
    if i ==len(res)-1:
        print('>')
        continue
    print(', ',end='')