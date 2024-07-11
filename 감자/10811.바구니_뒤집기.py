a = list(map(int,input().split()))
num_baskets = a[0] # number of baskets
count = a[1] # freq of changing baskets

basket = []
for i in range(num_baskets):
    basket.append(i+1)

method  = []
for i in range(count):
    method.append(list(map(int,input().split())))
    temp = basket[method[i][0]-1:method[i][1]]
    temp.reverse()
    basket[method[i][0]-1:method[i][1]] = temp

for i in range(len(basket)):
    print(basket[i],end=' ')