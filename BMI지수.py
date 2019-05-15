w =float(input("몸무게를 kg 단위로 입력 하시오 : "))
h = float(input("키를 m 단위로 입력 하시오 : "))
BMI = w/h**2
print("당신의 BMI = ",BMI)

if BMI<18.50:
    print("저체중 입니다.")

if 18.50<=BMI<=24.99:
    print("정상체중 입니다.")


if 24.99<BMI<=29.99:
    print("과체중 입니다.")


if 30<=BMI:
    print("비만 입니다.")


