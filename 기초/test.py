print("Hello World")
#입력
    #a = input("값을 입력하시오: ")
    #print(a)
#[변수]
b = '10'
c = 2
    #print(b+c) 타입 오류
print(int(b)+c)
    #bool, float 도 있음
a_bool = True
print(type(a_bool), a_bool)
print(type('a'),type("Hello")) #둘 다 str 타입
#자료형 변수
#{list}
a = [1,2,3,4,5]
print(a, a[0], a[1])
print(a[:2], a[3:])
b = []
b.append(1)
print(b)
b.append(a) #리스트 안에 리스트가 붙는 형태 1번 방 안에 리스트가 들어감, 여러형태 가능
b.append("Hello")
print(b, b[1])
b[0] = 5 #리스트 안 내용 변경 가능
print(b)
#{tuple}
a = (1,2,3)
print(type(a), a, a[2])
    #a[0] = 7 -> 오류발생 튜플은 데이터 변경 불가능
    #a.append("hello") -> append 역시 불가능
b = (1, (1,2) , [5, 4], "HELLO")
print(b) #튜플 역시 다양한 타입이 들어갈 수 있음
#{딕셔너리}
    #a = {'a':1, b:2, 'c':3, 4.5:5} -> 키값은 문자, 숫자만 / 벨류는 리스트 등 다양하게 가능
a = {'a':1, 2:[1,4,6], 'b':b}
print(type(a), a[2], a['b'])
a['d'] = 7 #데이터 추가 가능
print(a)
#{집합}
a = set([1,2,3,4])
b = set([1,1,1,2,4,5,3,4,4,3,4,4,3,2,5]) #중복이 없음
print(type(b), a, b)
c = set("python40s")
print(c) #순서는 **무작위**로 섞임
#[연산]
#{논리연산} or and not
#{비교연산} != > < ...etc
#(in)
a = ['a' , 2, [1,2], (3,4), {5:6, 'a':7}]
b = ('a' , 2, [1,2], (3,4), {5:6, 'a':7})
c = set([1,7,5,4,3,6,6,6,6])
print([1,2] in a, {5:6, 'a':7} in b, 7 in c, 'H' in 'HELlo') #자료형 변수, 문자열 안에 있는지 확인
#[조건]
