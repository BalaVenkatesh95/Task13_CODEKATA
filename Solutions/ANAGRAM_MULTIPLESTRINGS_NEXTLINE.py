number_of_strings = int(input())
count = 0
values = []
desired_string = "kabali"
# get inputs based on range
for _ in range(number_of_strings):
    values.append(input())

for name in values:
    if sorted(name) == sorted(desired_string):
        count = count + 1
print(count)
