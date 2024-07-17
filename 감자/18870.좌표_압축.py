from sys import stdin, stdout

# 시간초과
# count = int(stdin.readline().strip())
# points = list(map(int,stdin.readline().split()))
# sorted_list = sorted(set(points))
# for i in points:
#     print(sorted_list.index(i), end=" ")
    

# 시간초과
# numbers = list(map(int,stdin.readlines()[1:][0].split(' ')))
# set_numbers = set(numbers)
# list_set_numbers = list(set_numbers)
# sorted_list_set_numbers = sorted(list_set_numbers)
# for i in numbers:
#     stdout.write(str(sorted_list_set_numbers.index(i))+' ')

# dict 사용하기
numbers = list(map(int,stdin.readlines()[1:][0].split(' ')))
# sorted_numbers = sorted(numbers)
sorted_set_numbers = sorted(list(set(numbers)))
a = {}
for idx, i in enumerate(sorted_set_numbers):
    if i not in a.keys():
        a[i] = idx
# print(a)   
for i in numbers:
    print(a.get(i), end=' ')
    
