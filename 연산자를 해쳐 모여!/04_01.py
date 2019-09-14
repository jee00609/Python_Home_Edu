##변수 선언 부분
money, c500,c100, c50, c10 = 0,0,0,0,0

##메인 코드 부분
money = int(input("교환할 돈은 얼마?"))

#TIP) // 은 산술 연산자의 나누기(몫) 이다.
c500 = money//500
money%=500

c100 = money//100
money%=100

c50 = money//50
money%=50

c10 = money//10
money%=10

print("\n 오백원짜리 ==> %d 개" % c500)
print(" 백원짜리 ==> %d 개" % c100)
print("\n 오십원짜리 ==> %d 개" % c50)
print("\n 십원짜리 ==> %d 개" % c10)
print("\n 바꾸지 못한 잔돈 ==> %d 원 \n" % money)
