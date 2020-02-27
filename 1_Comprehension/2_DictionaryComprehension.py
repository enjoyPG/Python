#딕셔너리 컴프리헨션도 존재하며 쉽게 딕셔너리를 만들 수 있다.
fruit = "apple"
dic = { letter:fruit.count(letter) for letter in fruit}
print(dic)


#셋 컴프리헨션(셋은 유일한 키값만 가지는 자료구조)
mySet = { word for word in "banana" }
print(mySet)


#튜플 컴프리헨션은 존재하지 않는다. 출력된 타입을 보면 제너레이터 클래스이다.
#참고로 제너레이터 클래스는 파이썬의 시퀀스를 생성하는 객체로 range가 대표적이다. yield를 통해 리턴한다.
myTuple = ( num for num in range(10) if num%3==0)
print(type(myTuple))