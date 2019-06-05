def int_sum(put, n, sum) :
            sum=0
            n=1
            while n<=put :
                sum = sum+n
                n = n+1
            return sum

def besu_sum(start, end, a) :
            sum = 0
            for i in range (start, end +1) :
                if i%a==0 :
                    sum=sum+i
            return sum


while True :
    print("="*30)
    print("1. n까지 정수의 합")
    print("2. n~m까지 k의 배수의 합")
    print("3. 구구단 출력")
    print("종료")
    print("="*30)
    menu = int(input("정수를 입력하세요(1~4):"))

    if menu == 1 : ##1
        put = int(input("숫자를 입력 하시오 : "))
        print(int_sum(sum))

    if menu == 2 : ##2
        start = int(input("시작 값을 입력하세요."))
        end = int(input("끝 값을 입력하세요."))
        a = int(input("배수를 입력하세요."))
        hap = besu_sum(start, end, a)
print("%d에서 %d까지 %d의 배수의 합 = %d" %(start, end, a, hap))

    if menu == 3 : ##3
        print("3")
    if menu == 4 : ##4
        print("프로그램을 종료합니다.")
        break
