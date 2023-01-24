class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return(2*(self.length+self.breadth))
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("the area is:",x)
print("the perimeter is:",y)
l1=int(input("enter the length:"))
b1=int(input("enter the breadth:"))
o1=rectangle(l1,b1)
z=o1.area()
p=o.perimeter()
print("the area is:",z)
print("the perimeter is:",p)
if(x>z):
    print("first rectangle is greater")
else:
    print("second rectangle is greater")