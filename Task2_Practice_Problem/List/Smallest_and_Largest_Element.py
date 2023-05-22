#Program to find Smallest and Largest Element in the List.

# 1. By the use of min and max function of the list.
def smallLarge(List):
    print("Smallest element in the List=",min(List))
    print("Largest element in the List=",max(List))
    return

list=[10,2,5,4,58,98,74]
smallLarge(list)

# 2. By the use of sort() function.
def SmallLarge(list):
    list.sort()
    size=len(list)
    print("Smallest element in the List=", list[0])
    print("Largest element in the List=", list[size-1])
    return

list=[10,2,5,4,58,98,74]
SmallLarge(list)