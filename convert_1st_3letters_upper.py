#convert 1st 3 letters to upper and rest lower
#aishwarya swami
#012345678 9 101112131415 -> index numering
#string[start:end]  ->
'''start: The starting index (inclusive) of the slice.
end: The ending index (exclusive) of the slice.
'''
'''If you leave out start, it defaults to 0 (the beginning of the string). 
If you leave out end, it defaults to the length of the string (the end of the string).'''


str='aishwarya swami'
modified_str=str[:3].upper()+str[3:].lower()
print(modified_str)