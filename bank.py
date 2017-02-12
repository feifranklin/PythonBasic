principal=(int)(input("plz enter the amount: "))
apr=float(input("plz tell me the bank rate: "))

for i in range(1,11):
    principal = principal * (apr + 1)
    print("year %d: %f" %(i, principal))
    print("----------")

print("final value of my bank accout:", principal)
