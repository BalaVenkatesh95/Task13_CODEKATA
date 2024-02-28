user_input = int(input())
str_input = str(user_input)
sum_value = 0
product_value = 1
final_value = 0
for digit in str_input:
    sum_value = sum_value + int(digit)
    product_value = product_value * int(digit)
    final_value = sum_value + product_value

if final_value == user_input:
    print("Great")
else:
    print("no")
