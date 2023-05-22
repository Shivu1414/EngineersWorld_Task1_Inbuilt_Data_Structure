#Program to check element present in List or not.

def check(List,ele):
    value=False
    for el in List:
        if el==ele:
            value=True
    return value

List=[10,20,30,40,50,60]
ele=30
print(check(List,ele))