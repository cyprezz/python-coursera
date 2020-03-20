a = int(input())
b = int(input())
n = int(input())

cents = a * 100
totalCents = cents + b
totalPrice = totalCents * n

dollars = totalPrice // 100
cents = totalPrice % 100

print(dollars, cents)
