sec=int(input('초를 입력하세요.'))
year=sec//(24*60*60*365)
day=sec%(24*60*60*365)//(24*60*60)
hour=(sec%(24*60*60))//(60*60)
min=(sec%(60*60))//60
s=sec%60

print(year,'년 .',day,'일 .',hour,'시간 .',min,'분 .',s,'초')
