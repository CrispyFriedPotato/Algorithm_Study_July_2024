# -999 <= a, b, c, d, e, f <= 999
a, b, c, d, e, f = map(float, input().split())
# 1. 입력을 정수로 받으시면 안돼요. (정수) / (정수) = (정수)라서 중간에 계산이 틀릴 거예요. 

#     => 부동소수점 double로 받아주세요.

# 2. zero division 에러 조심하세요. (특히 부동소수점에서는 0으로 나눠도 에러가 안 뜨고, 그냥 INT_MIN이나 0이 나오니까 결과 확인해보세요)

#     => a, b, d, e 중에 0이 있는 경우 어떤 식을 사용해야 할지 고민해보세요.

# 3. 마지막에 double에서 int로 바로 형변환하시면 안돼요. int형 변환은 소수부를 없애는 방식으로 이루어지므로 2.99999도 3이 아니라 2로 바꿔줍니다.

#     => 내림이 아니라, 반올림해주세요.
# ax + by = c
# dx + ey = f

# dx + b *(d/a) y = (d/1)*c
# dx + ey = f

# y = {f - (d/a)*c}/{e - b*(d/a)}
# x = (c - b*y)/a

# y = (f - (d/a)*c)/(e - b*(d/a))
# print((f-e*y)/d,y)


# Brute Force
# 약 2000개의 경우의 수 이므로 brute force로 푸는거다.
# 2000 ^ 2
# for i in range(-999,1000,1):
#     for j in range(-999,1000,1):
#         if a*i + b*j == c:
#             if d*i + e*j == f:
#                 x = i
#                 y = j

print(x,y)
    