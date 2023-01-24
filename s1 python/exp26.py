n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
i=1
while(i<n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
        i=i+1
        print("gcd is:",gcd)