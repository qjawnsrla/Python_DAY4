# 리스트 : 연속적으로 저장되는 형태의 자료형
# 배열과 다르게 크기를 지정할 필요가 없음
# 읽고 쓰기가 가능(뮤터블)
# 같은 자료형일 필요가 없음
# [] 대괄호로 표시

number = [1,2,3,4,5]
fruits = ["apple", "banana", "orange"]
mixed = [1, 100, "apple", True, ["seoul", "korea"], ["안유진", "장원영", "이서", "레이"]]
print(number)
print(fruits[1])
print(f"아이브 멤버 : {mixed[5]}")   # 출력결과 : 아이브 멤버 : ['안유진', '장원영', '이서', '레이']
print(f"{mixed[4][1]}")     # 출력결과 : korea
print(f"{mixed[5][0]}")     # 출력결과 : 안유진
print(f"{mixed[5][1][0]}")  # 출력결과 : 장
print(f"{mixed[2][3]}")     # 출력결과 : l
print(f"{mixed[1:5]}")      # 출력결과 : [100, 'apple', True, ['seoul', 'korea']]
print(f"{mixed[5][:2]}")    # 출력결과 : ['안유진', '장원영']

# 리스트 연산자 : +, *
a = [1,2,3]
b = [4,5,6]
print(a + b)    # 연산자 오버로딩
print(a * 3)

# 리스트 요소 추가하기 : append(), insert()
# append(값) : 리스트의 마지막에 값을 추가
# insert(인덱스, 값) : 해당 위치에 값을 추가
a = [1,2,3,3]
a.append(4)
print(a)
a.append(99)
print(a)
a.insert(1, 100)    # 출력결과 : [1, 100, 2, 3, 4, 99]
print(a)

# 리스트 제거 : pop, remove, clear
# pop() : 인덱스를 넣지(쓰지) 않으면, 마지막 인덱스를 반환하고 값을 삭제 / 인덱스를 넣으면 해당 인덱스의 값을 삭제하고 보여줌
print(a.pop())
print(a.pop(1))
print(a)

# remove(값) : 해당하는 값을 지움, 값이 여러개인 경우는 인덱스가 낮은 걸 지움
a.remove(3)
print(a)

# del
del a[0]    # 인덱스로 값을 제거
print(a)

# clear
a.clear()   # 리스트 내의 모든 내용을 삭제하고 빈 리스트만 남김
print(a)

# 중복 제거하기
list_double = ["A", "B", "C", "D", "A", "D"]
list_new = []
for e in list_double:
    if e not in list_new:
        list_new.append(e)
print(list_new)

# 리스트의 순회
names = ["안유진", "장원영", "이서", "레이", "가을"]
for name in names:
    print(f"아이브 멤버 : {name}", end=" ")
print()

for i in range(len(names)):
    print(f"아이브 멤버 : {names[i]}", end=" ")