import turtle as t
n = int(input("숫자 입력"))
k = n*2

for i in range (k) :
    for i in range (n) :
        t.forward(100)
        t.right(360/n)
    t.right(180/k)
