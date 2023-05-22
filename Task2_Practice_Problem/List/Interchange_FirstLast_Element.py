#Interchange first and Last element of the list.

def interChange(List):
    size=len(List)
    first=List[0]
    List[0]=List[size-1]
    List[size-1]=first
    return List

List=[10,20,30,40,50]
print(interChange(List))
