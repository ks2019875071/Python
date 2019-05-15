n = int(input("정수를 입력 하시오:"))
factory = 1

for i in range(n, 1, -1) :
     print("%d*%d=%d" %(i, factory, factory*i))
     factory = factory*i
print("%d!=%d입니다."%(n,factory))
