size = int(input())
values = list(map(int, input().split()))
values.reverse()
string_values = [str(num) for num in values]
final_reversed_result = '->'.join(string_values)
print(final_reversed_result)
