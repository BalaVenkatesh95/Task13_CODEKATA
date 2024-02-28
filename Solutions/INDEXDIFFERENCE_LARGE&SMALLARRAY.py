total_numbers = int(input())
values = list(map(int, input().split()))
min_value = min(values)
max_value = max(values)
index_of_min_value = values.index(min_value)
index_of_max_value = values.index(max_value)
difference = index_of_max_value - index_of_min_value
print(difference)