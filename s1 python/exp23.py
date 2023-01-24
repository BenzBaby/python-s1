str3=input("enter a string")
print(str3)
dict={}
for i in str3:
    if i in dict:
        dict[i]+=1
        print(dict)
    else:
        dict[i]=1

for j,k in dict.items():
    print(j,k)