string_input = input()
char_frequency = {}
final_string = ""
# Count the frequency of each character
for char in string_input[:]:
    char_frequency[char] = char_frequency.get(char, 0) + 1
min_char = min(char_frequency, key=char_frequency.get)

for key, value in char_frequency.items():
    if value == 1:
        final_string = final_string + key
print(final_string)
