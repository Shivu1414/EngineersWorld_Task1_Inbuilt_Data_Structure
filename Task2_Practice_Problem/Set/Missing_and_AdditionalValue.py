#missing and additional value by set.
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print("Missing value in set1=",set2-set1)
print("Additional value in set1=",set1-set2)

print("Missing value in set2=",set1-set2)
print("Additional value in set2=",set2-set1)
