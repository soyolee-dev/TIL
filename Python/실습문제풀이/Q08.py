# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]

#1. 최댓값 first를 지정해 먼저 구해본다.
first = numbers[0]

for i in numbers:
    if i > first:
        first = i

#2. 두번째 최댓값 second를 지정해 first보다 작은 값으로 지정한다.
second = numbers[0]

for a in numbers:
    if a >= second and a < first:
        second = a

print (second)