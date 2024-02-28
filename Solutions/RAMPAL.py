number = int(input())
str_number = str(number)
if number < 0:
    first_digit = str_number[0]
    second_digit = str_number[-1]
    sum_value = int(first_digit) + int(second_digit)
    if sum_value % 4 == 0:
        print("yes")
    else:
        print("no")
else:
    first_digit = str_number[-1]
    second_digit = str_number[-2]
    sum_value = int(first_digit) + int(second_digit)
    if sum_value % 4 == 0:
        print("yes")
    else:
        print("no")
