from sys import stdin

# def fib(n):
#     # global count_fib
#     if n==1 or n==2:
#         return 1
#     elif n >2 :
#         return (fib(n-1) + fib(n-2))
#     else:
#         return 0
def fib_dp(n):
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n] 

n = int(stdin.readline())
memo = [None] * 50
memo[1] = 1
memo[2] = 1

# count_fib = fib(n)
# fib_dp(n)
print(fib_dp(n) , n-2)

# python 변수는 scope based이다. 이것은 one cannot access a value declared inside a function.을 의미
# But you can access a variable declared outside a func.