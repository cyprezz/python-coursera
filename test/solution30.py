n = int(input())
m = int(input())
k = int(input())

if k <= n * m:
    if k % n == 0 or k % m == 0:
        val = 'YES'
    else:
        val = 'NO'
else:
    val = 'NO'

print(val)
