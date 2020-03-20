n = int(input())

part1 = n // 100
part2 = n % 100

num1 = part1 // 10
num2 = part1 % 10

num3 = part2 // 10
num4 = part2 % 10

part2Rev = int(str(num4) + str(num3))

sum1 = num1 + num2
sum2 = num3 + num4

res = part1 - part2Rev


res = res ** 2
print(0 ** res)
