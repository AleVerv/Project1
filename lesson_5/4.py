n = int(input())
sum = 0
i = 1
while i <= n:
    sum+= i**3
    i = i+1
print(sum)


sum = 0
i = 1
for i in range(0, n):
    i = i+1
    sum += i**3
print(sum)