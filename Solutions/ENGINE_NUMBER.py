number_plate = input()
string_list = []
integer_list = []
engine_number = 0
for char in number_plate:
    if char.isdigit():
        integer_list.append(char)
    else:
        string_list.append(char)

for number in integer_list:
    engine_number = engine_number + int(number)
print(engine_number)
