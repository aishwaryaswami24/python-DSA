#list find out duplicate values in it
lst=[1,2,3,4,5,5,5,4]


seen=set()
duplicates=set()

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)


#print(seen)
#converted set to list
print('seen list:',list(seen))
#print(duplicates)
print('duplicates list:',list(duplicates))


#find out even values in list and print
lst=[1,2,3,4,5,6]

even_lst=[]

