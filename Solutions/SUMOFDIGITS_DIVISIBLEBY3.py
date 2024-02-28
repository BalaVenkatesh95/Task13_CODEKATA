user_input = int(input())
str_input = str(user_input)
sum_value = 0
for digit in str_input:
    sum_value = sum_value + int(digit)
if sum_value % 3 == 0:
    print("yes")
else:
    print("not")
