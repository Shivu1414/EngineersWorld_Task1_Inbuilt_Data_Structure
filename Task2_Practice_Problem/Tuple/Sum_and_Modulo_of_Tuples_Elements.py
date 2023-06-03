#Sum of tuple Elements
tuple1=(1,2,3,4,5,65,95)
print(tuple1)

sum=0
for val in tuple1:
    sum=sum+val

print("Sum of Tuple Elements= ",sum)


#Modulo of Two tuples Elements
tup1=(10,20,30,40,50)
tup2=(5,3,4,5,6)

list=[]
for val1, val2 in zip(tup1,tup2):
    list.append(val1%val2)

list=tuple(list)
print(list)
# print(type(list))
