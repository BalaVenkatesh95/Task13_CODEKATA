user_input = int(input())
str_input = str(user_input)
product_value = 1
for digit in str_input:
    product_value = product_value * int(digit)
print(product_value)
