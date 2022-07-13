# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while문

a = 1
result = 1
n = int(input())

while a <= n:
    result *= a
    a += 1
print(result)


# 2) for문

a = 1
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i
    i += 1
print(result)