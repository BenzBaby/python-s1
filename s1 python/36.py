class bank:
    def __init__(self,acc,name,acctype):
        self.acc=acc
        self.name=name
        self.acctype=acctype
        self.bal=0
    def showamount(self):
        print("account holder name:",self.name)
        print("account number:",self.acc)
        print("account account type:",self.acctype)
        print("your balance:",self.bal)
    def depo(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("enter account name:")
a=int(input("enter your account number:"))
t=input("enter your account type:")
o=bank(a,n,t)
o.showamount()
while(True):
    print("\n menu")
    print("\n1.deposit")
    print("\n2.withdraw")
    c=int(input("enter your choice:"))
   # d=0
    if(c==1):
        d=int(input("enter the amount to deposit"))
        print("your total balance amount is:",o.depo(d))
    elif(c==2):
        w=int(input("enter the amount to be withdrawn:"))
        if(w>d):
            print("insufficient balance.")
        else:
            print("your total balance amount is:",o.withdraw(w))
    else:
        print("enter a valid choice")