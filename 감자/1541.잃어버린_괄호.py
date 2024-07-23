from sys import stdin

# 괄호가 필요한 때는 ++++ 중 -가 있을때, ---- 중 + 가 있을때라고 생각함

formulas = stdin.readline()
if '-' in formulas:
    form = formulas.split('-')
    result = sum(map(int,form[0].split('+')))
    for j in form[1:]:   
        result -= sum(map(int,j.split('+')))
else:
    result = sum(map(int,formulas.split('+')))

print(result)


