number_of_users = int(input())
username_values = list(map(str, input().split()))
final_user_list = []
Verified_list = []
for value in username_values:
    if value not in final_user_list:
        final_user_list.append(value)
        Verified_list.append("Verified")
    else:
        new_value = value + "1"
        final_user_list.append(new_value)
        Verified_list.append(new_value)
user_values = " ".join(Verified_list)
print(user_values)
