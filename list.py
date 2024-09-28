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


#two list find duplicates from it
lst1=[1,2,3,4,5,6]
lst2=[2,3,4,0,9,0,4]

duplicates=[]

for i in lst1:
    if i in lst2:
        duplicates.append(i)
print(duplicates)

#2nd way
lst1=[1,2,3,5,6]
lst2=[2,3,4,6,1]
duplicates=set(lst1).intersection(lst2)
print(list(duplicates))


#findout duplicates from single list
lst=[1,2,3,3,4,5,1,1]
print(set(lst))#removed duplicates from list

seen=set()
dup=set()
for i in lst:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(list(seen))
print(list(dup))

