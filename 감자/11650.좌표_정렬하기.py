import sys
n = int(sys.stdin.readline())
coord = []
for i in range(n):
    coord.append(list(map(int,sys.stdin.readline().split())))

sorted_coord = sorted(coord)

for i in range(n):
    print(sorted_coord[i][0],sorted_coord[i][1])
    

# Other's Answer

def sort_num(n):
    x, y = n.split()
    return int(x) + int(y)/1000000

coord = sys.stdin.readlines()[1:]
coord.sort(key=lambda n: sort_num(n)) # key의 lamda는 이해하기가 좀 어려움
print("".join(coord))