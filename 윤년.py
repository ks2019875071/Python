years = int(input("연도를 입력 하시오."))

if years%4==0 and years%100!=0 or years%400 ==0 :
    print(years,"년은 윤년입니다.")
else :
    print(years,"년은 윤년이 아닙니다.")
