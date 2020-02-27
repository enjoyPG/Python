#제너레이터는 파이썬의 시퀀스를 생성하는 함수다.
#range()함수가 대표적이다. 다만 return대신 yield를 사용하고
#일반 함수에서 return으로 값을 반환하지만 제너레이터에서는 yield로 값을 반환한다.
#return에서는 값을 한 번만 반환하지만 제너레이터에서는 시퀀스를 생성하는 객체이므로
#반복적으로 계속 yield를 통해 값을 반환한다.
#제너레이터의 가장 적절한 예인 range()함수 구현해보자.

def myRange(start, end, step=1):
    num = start
    while num<end:
        yield num;
        num+=step;

numList = myRange(1, 10, 2)
print(type(numList))
        
for i in myRange(5, 10):
    print(i)