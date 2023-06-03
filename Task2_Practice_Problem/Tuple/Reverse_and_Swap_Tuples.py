# Reverse the Tuple

tuple1=(10,20,30,40,50)
tuple1=tuple1[::-1]
print(tuple1)

# Method2
list=[]
tuple2=(10,20,30,40,50)
length=len(tuple2)

for i in range(length-1,-1,-1):
    list.append(tuple2[i])

tuple2=tuple(list)
print(tuple2)

# Swap two tuples
tup1=(10,20,30,40,50)
tup2=(70,80,60,10,20)
tup1,tup2=tup2,tup1
print(tup1)
print(tup2)