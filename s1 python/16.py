n=int(input("enter the no of elements:"))
print("enter the elements")
list=[]
for i in range(0,n):
    element=int(input())
    if(element>100):
      list.append("over")
    else:
       list.append(element)
print(list)