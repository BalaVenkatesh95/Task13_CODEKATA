number = int(input())
number_str = str(number)
remove_duplicates = set(number_str)
final_length = len(remove_duplicates)
if final_length == 2:
    print("Saturated")
else:
    print("Unsaturated")
