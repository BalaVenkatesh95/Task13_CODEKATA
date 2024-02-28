no_of_tickets = int(input())
ticket_numbers = list(map(int, input().split()))
date = int(input())
result_list = []
for ticket in ticket_numbers:
    if ticket % date == 0:
        result_list.append(1)
    else:
        result_list.append(0)

for i in range(len(result_list) - 1):
    print(result_list[i], end=" ")
if result_list:
    print(result_list[-1], end="")
