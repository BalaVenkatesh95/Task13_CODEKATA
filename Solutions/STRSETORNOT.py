string_input01, string_input02 = map(str, input().split())
if string_input01 in string_input02 or string_input02 in string_input01:
    print("Yes")
else:
    print("No")
