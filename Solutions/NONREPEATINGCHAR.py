string_input = input()
char_count = {}

for char in string_input:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

least_occurred_char = min(char_count, key=char_count.get)
print(least_occurred_char)
