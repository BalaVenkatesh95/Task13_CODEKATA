n, m = map(int, input().split())
while m != 0:
    n, m = m, n % m
if n == 1:
    print(1)
else:
    print(0)
