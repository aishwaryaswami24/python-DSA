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


#find out even & odd values in list and print
lst=[1,2,3,4,5,6]

even_lst=[]
odd_lst=[]

for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)

print(even_lst)
print(odd_lst)


##two list find duplicates from it
lst1=[1,2,3]
lst2=[2,3,4]
