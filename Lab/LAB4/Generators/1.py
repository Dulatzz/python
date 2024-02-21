def squares(n):
    i = 1
    while i <= n:
        yield i*i
        i += 1

n = int(input())
for i in squares(n):
    print(i)