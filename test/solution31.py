n = int(input())

if n <= 10:
    number = n
else:
    number = n % 10

if 10 <= n <= 19:
    suff = 'korov'
else:
    if number == 1:
        suff = 'korova'
    elif 2 <= number <= 4:
        suff = 'korovy'
    else:
        suff = 'korov'

print(n, suff)
