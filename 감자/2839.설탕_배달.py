kilo = int(input())

min_bongji = 1700

for i in range(kilo//3+1):
    for j in range(kilo//5+1):
        if 3*i + 5*j == kilo:
            if i+j < min_bongji:
                min_bongji = (i+j)
if min_bongji == 1700:
    print(-1)
else:             
    print(min_bongji)

