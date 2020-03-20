a = int(input())
b = int(input())

flats = b - a + 1

if a != 1:
    if (a - 1) // flats == 0:
        val = 'NO'
    else:
        if (a - 1) % flats == 0:
            val = 'YES'
        else:
            val = 'NO'
else:
    val = 'YES'

print(val)
