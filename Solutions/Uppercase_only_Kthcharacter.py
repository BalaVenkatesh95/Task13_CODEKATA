string_input, K = input().split()
K_int = int(K)
altered_string = []

if K_int ==0:
    print(string_input)
else:
    for index, char in enumerate(string_input):
        if (index + 1) % K_int == 0:
            altered_string.append(char.upper())
        else:
            altered_string.append(char)

altered_string_result = ''.join(altered_string)
print(altered_string_result)