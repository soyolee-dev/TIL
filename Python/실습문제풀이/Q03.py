# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# 1) while문

a = 0
result = 0
n = int(input())

while a <= n:
    result += a
    a += 1
print(result)


# 2) for문

n = int(input())
result = 0

for i in range(1, n+1):
    result += i
print(result)