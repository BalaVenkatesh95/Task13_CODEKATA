string_input = input()
char_count = {}
final_string = []
for char in string_input:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1
for key, value in char_count.items():
    if value > 1:
        final_string.append(key)
final_output = " ".join(final_string)
if not final_string:
    print(-1)
else:
    print(final_output)
