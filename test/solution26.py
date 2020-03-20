a = int(input())
val = ''

if a % 4 == 0:
    val = 'YES'
    if a % 100 == 0 and a % 400 != 0:
        val = 'NO'
    elif a % 100 == 0 and a % 400 == 0:
        val = 'YES'
else:
    val = 'NO'

print(val)
