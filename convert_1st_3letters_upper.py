# #convert 1st 3 letters to upper and rest lower
# #aishwarya swami
# #012345678 9 101112131415 -> index numering
# #string[start:end]  ->
# '''start: The starting index (inclusive) of the slice.
# end: The ending index (exclusive) of the slice.
# '''
# '''If you leave out start, it defaults to 0 (the beginning of the string).
# If you leave out end, it defaults to the length of the string (the end of the string).'''
#
#



s='aishwarya swami'
convert=s[:3].upper()+s[3:].lower()
print(convert)

lst=[1,2,3,3,2,3]
seen=set()
dup=set()
for i in lst:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(list(dup))
#removed duplicates
lst=set(lst)
print(lst)

#even&odd
ls=[1,2,3,4,5,6]

even_ls1=[]
odd_ls2=[]
for i in ls:
    if i%2==0:
        even_ls1.append(i)
    else:
        odd_ls2.append(i)
print(even_ls1)
print(odd_ls2)






