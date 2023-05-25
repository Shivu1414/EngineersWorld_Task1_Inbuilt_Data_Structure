#min value in set.
def Min(set):
    print(min(set))

set={10,20,30,40}
Min(set)

#Max value in set.
def Max(set1):
    print(max(set1))

set1={10,20,30,40,50}
Max(set1)

# remove element from set one by one.
def Remove(set2):
    while(set2):
        set2.pop()
        print(set2)

set2={10,20,30,"shiv"}
Remove(set2)

#Remove element from set.
def RemoveElement(set3,ele):
    set3.remove(ele)

set3={10,20,30,50,"Shiv"}
RemoveElement(set3,10)
print(set3)