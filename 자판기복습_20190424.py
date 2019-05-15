insert = int(input("동전을 투입 하시오."))
price = int(input("물건 값을 입력 하시오."))

coin = insert-price
coin500 = coin//500
coin100 = (coin%500)//100
coin50 = (coin%100)//50

print("500원 동전의 개수 = ",coin500)
print("100원 동전의 개수 = ",coin100)
print("50원 동전의 개수 = ",coin50)
