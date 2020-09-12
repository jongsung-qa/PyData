# if, elif, else
x=10
if x < 0:
    print("It's negative")
elif x ==0:
    print("Equal to zero")
elif 0 < x < 5:
    print("Positive but smaller than 5")
else:
    print("Positive and larger than or equal to 5")

# for_continue
sequence = [1,2, None, 4, None,5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
print(total)

# for_break : : for문이 중첩일경우 해당 for문만 탈출
sequence = [1,2,0,4,6,5,3,1]
total_b = 0
for value in sequence:
    if value == 5:
        break
    total_b += value
print(total_b)

# while
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x//2
print(total)

# pass : 아무섯도 하지 않음 => 블록 내에서 어떤 작업도 실행하지 않을때 사용, ex)코드를 나중에 작성하기 위해 예약
if x < 0:
    print('negative')
elif x == 0:
    # Todo : 작성
    pass
else:
    print('positive')

# 삼항표현식
# if condition:
#    value = true-expr
# else:
#   value = false-expr
# value = true-expr if condition else false-expr