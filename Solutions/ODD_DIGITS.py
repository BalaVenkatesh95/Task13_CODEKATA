user_input = input()
odd_list = []
for digit in user_input:
    if int(digit) % 2 != 0:
        odd_list.append(digit)

if not odd_list:
    print(-1)
else:
    for i in range(len(odd_list) - 1):
        print(odd_list[i], end=" ")
    if odd_list:
        print(odd_list[-1], end="")
