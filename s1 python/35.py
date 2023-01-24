class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def peremeter(self):
        return (2 * (self.length + self.breadth))


l = int(input("Enter the  lenght of first rectangle"))
b = int(input("Enter the breadth of first rectangle"))
x = rectangle(l, b)
y = x.area()
z = x.peremeter()
print("The area of first rectangle is", y)
print("The peremeter of first rectangle is", z)
l1 = int(input("Enter the lenght lenght of second rectangle"))
b1 = int(input("Enter the breadth of second rectangle"))
x1 = rectangle(l1, b1)
y1 = x1.area()
z1 = x1.peremeter()
print("The area of second rectangle is", y1)
print("The peremeter of second rectangle is", z1)
if (y > y1):
    print("The first rectangle has more area  ")
else:
    print("The second rectangle has more area  ")
