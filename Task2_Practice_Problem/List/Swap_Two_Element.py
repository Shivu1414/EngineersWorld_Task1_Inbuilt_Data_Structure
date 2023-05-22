#Program to swap two element of the List.

def swapElement(List,Pos1,Pos2):
    List[Pos1],List[Pos2]=List[Pos2],List[Pos1]
    return List

List=[10,20,30,40,50,60]
pos1=2
pos2=4
swapElement(List,pos1,pos2)
print(List)