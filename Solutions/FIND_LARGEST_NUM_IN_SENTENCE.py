import re
sentence = input()
numbers = re.findall(r'\d+', sentence)
number_list = []
for num in numbers:
    int_num = int(num)
    number_list.append(int_num)
maximum_number = max(number_list)
print(maximum_number)
