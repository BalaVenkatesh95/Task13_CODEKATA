string_input_01, string_input_02 = input().split()
result_string_01 = ''
result_string_02 = ''
for char in string_input_01:
    if char in string_input_02:
        result_string_01= result_string_01+char.upper()
    else:
        result_string_01 = result_string_01 + char
for char in string_input_02:
    if char in string_input_01:
        result_string_02 = result_string_02+char.upper()
    else:
        result_string_02 = result_string_02 + char

final_output = result_string_01+" "+result_string_02
print(final_output)


