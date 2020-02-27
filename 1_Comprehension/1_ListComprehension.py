#컴프리헨션(Comprehension-함축)은 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 컴팩트한 방법이다.


#1. 컴프리헨션의 기본적인 사용 - [표현식 for 항목 in iterator(순회가능한 객체)]
nList1 = [number for number in range(5)]
print(nList1)

nList2 = [number * 2 for number in range(5)]
print(nList2)




#2. 컴프리헨션과 조건문의 만남
nList3  = [number for number in range(10) if number % 5 == 0]
print(nList3)




#3. for 루프 중첩
rows = range(1,5)
cols = range(1,3)

# for 루프 중첩을 통해 2차원 형태의 데이터 표현
for row in range(1,5):
    for col in range(1,3):
        print(row, col)
# 컴프리헨션을 적용해 간단히 튜플 형태로 cells에 저장
cells = [(row, col) for row in rows for col in cols] 
print(cells)

#아래와 같이 바로 언패킹도 가능하다
for row, col in cells:
    print(row, col)