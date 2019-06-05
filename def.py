
start = int(input("시작 값을 입력하세요."))
end = int(input("끝 값을 입력하세요."))
a = int(input("배수를 입력하세요."))

def a_sum(start, end, a) :
    sum = 0
    for i in range (start, end +1) :
        if i%a==0 :
            sum=sum+i
    return sum

hap = a_sum(start, end, a)
print("%d에서 %d까지 %d의 배수의 합 = %d" %(start, end, a, hap))
