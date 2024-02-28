input_string = input()
reversed_string = input_string[::-1]
result_string = "-".join(reversed_string)

if result_string.endswith("-"):
    result_string = result_string[:-1]
print(result_string)
