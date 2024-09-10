lst=[1,1,1,1,3,4,5,5,6,7,0,4]
#list converted into set
unique_no=set(lst)
print(unique_no)

#set convert to list if you want to
unique_no=list(set(lst))
print(unique_no)

print(f"Duplicates values removed from the list")

#Using dict.fromkeys()
lst1=[1,2,3,4,4,9,9,9,4]
remove_duplicates=list(dict.fromkeys(lst1))
print(remove_duplicates)

#using a for loop
lst2=[1,1,1,2,3,4,4,4,5,6,7,9,0,0,0]
empty_lst=[]
for i in lst2:
    if i not in empty_lst:
        empty_lst.append(i)
print(f'Previous list: ',lst2)
print(f'Current list: ',empty_lst)

