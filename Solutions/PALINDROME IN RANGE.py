size = int(input())
palindrome_list = []
for num in range(1, size + 1):
    num_str = str(num)
    reversed_num = num_str[::-1]
    if num_str == reversed_num:
        palindrome_list.append(num_str)
print(len(palindrome_list))
