start = int(input("시작 값을 입력하세요."))
end = int(input("끝 값을 입력하세요."))
a = int(input("배수를 입력하세요."))
sum = 0

#for문으로
for i in range (start, end +1) :
    if i%a==0 :
        sum=sum+i
print("%d에서 %d까지 %d의 배수의 합 = %d" %(start, end, a, sum))

#while문으로
sum = 0
i = start
while i <= end :
    if i%a==0 :
        sum = sum+i
    i = i+1
print("%d에서 %d까지 %d의 배수의 합 = %d" %(start, end, a, sum))
