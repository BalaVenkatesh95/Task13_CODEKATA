string_01, string02 = map(str, input().split())
result_string = ""
for char in string_01:
    if char not in string02:
        result_string = result_string + char

if result_string == "":
    print(-1)
else:
    print(result_string)
