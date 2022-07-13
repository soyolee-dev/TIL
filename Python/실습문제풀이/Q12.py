# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

# 주어진 문자열 word
word = input()

# a를 제외한 알파벳이 모이는 문자열
no_a = ""

# a를 제외한 알파벳 모으기
for i in word:
    if i != "a":
        no_a += i

print(no_a)