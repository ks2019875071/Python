z_list = []

import random

for i in range(5) :
    z_list.append(random.randint (1, 100))

e_list = []

for i in range (0, 4) :
    for z in range(i+1, 5) :
        if z_list[i] > z_list[z] : ## z리스트의 i번째보다 z번째가 작을 때
            temp = z_list[i] ## 임시 변수 temp에 z리스트의 i번째를 넣는다
            z_list[i] = z_list[z] ## z리스트의 i 자리에 z를 넣는다
            z_list[z] = temp
            

print(z_list)
