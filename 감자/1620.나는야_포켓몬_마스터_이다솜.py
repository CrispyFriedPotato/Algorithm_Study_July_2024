import sys
n , m = map(int,sys.stdin.readline().split())
n_list = []
n_dict = {}
for i in range(n):
    n_list.append(sys.stdin.readline().strip())
    n_dict[n_list[i]] = i
for s in sys.stdin:
    i = s.strip()
    if 48 <= ord(i[0]) and ord(i[0]) <= 57:
        print(n_list[int(i)-1])
    else:
        print(n_dict[i]+1)
