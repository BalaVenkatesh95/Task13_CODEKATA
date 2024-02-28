input_data = input()
vowels = "AEIOUaeiou"
result = ""
for char in input_data[:]:
    if char not in vowels:
        result = result+char
reversed_result = result[::-1]
if not reversed_result:
    print(-1)
else:
    print(reversed_result)
