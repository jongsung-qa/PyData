# tuple
# 변경 불가능한 순차 자료형
# 중첩된 튜플 정의가 가능
# 튜플에 저장된 객체 자체는 변경이 가능하지만, 한번 생성되면 각 원소만을 따로 변경하는 것은 불가능

# 값 분리하기
tup = (4,5,6)
a,b,c = tup
print(b)

a,b=1,2
b,a=a,b
print(a)
print(b)

seq=((1,2,3),(4,5,6),(7,8,9))
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))

# 몇몇 값을 분리하고 나서 나머지 값들 한꺼번에 분리할때는 *를 앞에 붙인 리스트 변수를 사용
values=1,2,3,4,5
a,b,*rest = values
print(a,b)
print(rest) # 리스트 형식으로 출력

# 메서드 : count, index
a=(1,2,2,3,2,4,2)
print(a.count(2))

# list : 크기나 내용의 변경이 가능
gen = range(10)
print(gen)

# 메서드 : append, insert(1,'value'), pop, extend, sort
