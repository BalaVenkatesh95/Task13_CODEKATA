number = int(input())
str_number = str(number)
first_digit = str_number[0]
second_digit = str_number[1]
sum_value = int(first_digit) + int(second_digit)
str_sum = str(sum_value)
if str_sum in str_number:
    print(1)
else:
    print(0)
