N, M = map(int, input().split())
difference = N - M

if difference == 0:
    print("even")
elif difference % 2 == 0:
    print("even")
else:
    print("odd")
