a = input()

total = 0
for i in range(len(a)):
    if a[i] == 'j':
        if a[i-1] == 'l':
            continue
        if a[i-1] == 'n':
            continue
    if a[i] == '=' or a[i] == '-':
        if a[i-1] == 'z':
            if a[i-2] == 'd':
                total -=1
        continue
    total +=1
print(total)