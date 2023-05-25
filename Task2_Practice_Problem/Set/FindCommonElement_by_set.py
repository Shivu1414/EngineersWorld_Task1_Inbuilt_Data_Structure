# Find common element in three lists using set.
def commonElement(list1,list2,list3):
    s1=set(list1)
    s2=set(list2)
    s3=set(list3)
    fresult=s1&s2&s3
    # result1=s1.intersection(s2)
    # fresult=result1.intersection(s3)
    return fresult

list1=[2,4,5,6,7,9,10,12,16]
list2=[2,4,6,10,18,23]
list3=[2,4,8,11,13,13]
fset=commonElement(list1,list2,list3)
print(fset)
print(type(fset))