rooms = int(input())
applicants = list(map(int,input().split()))
supervisors = list(map(int, input().split()))

total = 0
for i in range(rooms): # head_supervisor
    applicants[i] -= supervisors[0]
    total +=1

for i in range(rooms): # vice_supervisor
    
    if applicants[i] < 1:
        continue
    if applicants[i] <= supervisors[1]:
        applicants[i] -=supervisors[1]
        total+=1
    else:
        total += applicants[i]//supervisors[1]
        if applicants[i]%supervisors[1]>0:
            total += 1
print(total)