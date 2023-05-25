#Program to Reverse the given List.

def reverse(List):
    List1=[]
    size=len(List)
    for i in range(size-1,-1,-1):
        List1.append(List[i])
    return List1

List=[10,20,30,40,80,65,95]
print(reverse(List))