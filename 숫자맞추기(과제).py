import random

ball = 0 ## 볼 횟수
strike = 0 ## 스트라이크 횟수

z_list = [] ## 랜덤으로 나오는 숫자 리스트
for i in range (3) :
    z_list.append(random.randint(1, 9))
print(z_list)

while strike!=3 :
    your_list = [] ## 입력하는 숫자 리스트
    your_list.append(int(input("첫번째 정수를 입력 하세요.")))
    your_list.append(int(input("두번째 정수를 입력 하세요.")))
    your_list.append(int(input("세번째 정수를 입력 하세요.")))

    for i in range (0, 3, 1) :
        if z_list[i]==your_list[i] :
            strike = strike+1
    print("%d 스트라이크 입니다." %(strike))

if strike==3 :
    print ("게임 종료")
