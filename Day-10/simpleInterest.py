def simple_interest(principal,rate,time):
    return (principal * rate * time)/100

P=float(input("Enter principal amount : "))
R=float(input("Enter rate of interest : "))
T=float(input("Enter time in years : "))

print("Simple Interest is : ",simple_interest(P,R,T))
