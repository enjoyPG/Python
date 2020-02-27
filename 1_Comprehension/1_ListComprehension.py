#컴프리헨션(Comprehension-함축)은 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 컴팩트한 방법이다.

#컴프리헨션의 기본적인 사용 - [표현식 for 항목 in iterator(순회가능한 객체)]
nList1 = [number for number in range(5)]
print(nList1)

nList2 = [number * 2 for number in range(5)]
print(nList2)


#컴프리헨션과 조건문의 만남
nList3  = [number for number in range(10) if number % 5 == 0]
print(nList3)

