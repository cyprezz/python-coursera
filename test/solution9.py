n = int(input())

first = n // 100
second = n // 10 % 10
third = n % 10

result = first + second + third

print(result)
