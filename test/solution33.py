x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 > 0 and x2 > 0:
    if y1 > 0 and y2 > 0:
        val = 'YES'
    elif y1 < 0 and y2 < 0:
        val = 'YES'
    else:
        val = 'NO'
elif x1 < 0 and x2 < 0:
    if y1 > 0 and y2 > 0:
        val = 'YES'
    elif y1 < 0 and y2 < 0:
        val = 'YES'
    else:
        val = 'NO'
else:
    val = 'NO'

print(val)
