string_input = input()
result_string = ""
for index, char in enumerate(string_input):
    if index == 0 or index == 2:
        result_string = result_string + char
print(result_string)
