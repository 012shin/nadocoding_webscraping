# quiz #3

url = 'http://naver.com'

code = url.split('://')[1].split(".")[0]
e_count = 0
for i in range(len(code)):
    if code[i].lower() == 'e':
        e_count += 1
# count 함수도 존재함 code.count('e')
# print(code.count('e'))
print('#quiz3')
print(f"생성된 비밀번호 : {code[:3]}{len(code)}{e_count}!")

# quiz 4
from random import *

id = [i for i in range(1, 21)]
# print(id)
shuffle(id)
chicken = sample(id, 1)

if chicken in id:
    id.remove('chicken')

coffee = sample(id, 3)
print('quiz2')
print('--------당첨자 발표-----------')
print(f"치킨당첨자 : {chicken}")
print(f'커피당첨자 : {coffee}')

cnt = 0  # 총 탑승 승객 수

for i in range(1, 51):
    passenger = randint(5, 50)
    if passenger <= 15:
        print(f"[o]{i + 1}번째 손님 (소요시간:{passenger}분)")
        cnt += 1
    else:

        print(f"[ ]{i+1}번째 손님 (소요시간:{passenger}분)")

print(f"총 탑승 승객 {cnt}분")


def std_weight(height,gender):
    if gender == '남자':
        std_weight = height**2* 22
    elif gender == "여자":
        std_weight= height**2 * 21
    return std_weight

height = 175
gender = '남자'
print('\n\nquiz#6')
print(f"{height}cm {gender}의 표준 체중은 {std_weight(height/100,gender)}kg")


class SoldoutError(Exception):
    pass
chicken = 10
waiting = 1
while True:
    try:
        print(f"남은 치킨: {chicken}")
        order = int(input('치킨 몇 마리 주문하시겠습니까?'))
        if order > chicken:
            print('재료가 부족합니다')
        elif order<=0:
            raise ValueError
        else:
            print(f'[대기번호{waiting}번] {order}마리 주문이 완료되었습니다.')
            waiting+=1
            chicken -= order
        if chicken == 0:
            raise SoldoutError
    except ValueError:
        print('잘못된 값을 입력하셨습니다.')
    except SoldoutError:
        print('재고가 모두 소진되었습니다.')
        break
    finally:
        print('찾아주셔서 감사합니다.')


