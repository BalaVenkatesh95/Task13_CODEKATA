string_input = input()
odd_index_string = ""
even_index_string = ""

for index, char in enumerate(string_input):
    if index == 0:
        even_index_string = even_index_string + char
    elif index % 2 == 0:
        even_index_string = even_index_string + char
    else:
        odd_index_string = odd_index_string + char
print(even_index_string, odd_index_string)

'''In coding index starts from zero but as per position we start from 
one, so printing even_index_string for odd position and odd index string for
even position
(0 is first position and 1 is second position)
'''

