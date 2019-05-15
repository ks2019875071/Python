insert = int(input("동전을 투입 하시오"))
price = int(input("물건 값은 얼마입니까?"))
change = insert - price

coin500 = change//500
coin100 = (change%500)//100

print("거스름돈은 ",change," 입니다.")
print("500원 동전은 ",coin500,"개, ","100원 동전은 ",coin100,"개 입니다.")
