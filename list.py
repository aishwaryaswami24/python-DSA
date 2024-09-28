#list find out duplicate values in it
lst=[1,2,3,4,5,5,5,4]

seen=set()
duplicates=set()

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print('Seen list:',list(seen))
print('Duplicates list:',list(duplicates))

