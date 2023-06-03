tup1=(3,5,4,2,7,1,6,9)
print("Original tuple= ",tup1)

length=len(tup1)
print(length)

num=int(input("Enter no. of value you want= "))

print("Enter 1 for min. value")
print("Enter 2 for max. value")
value=int(input())

list=[]
if value==1:
    tup1=sorted(tup1)
    for i in range(0,num):
        list.append(tup1[i])
elif value==2:
    tup1 = sorted(tup1)
    for i in range(length-num,length):
        list.append(tup1[i])

print(list)


