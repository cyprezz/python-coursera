cell1 = int(input())
cell2 = int(input())
cell3 = int(input())
cell4 = int(input())

if cell1 % 2 == 0 and cell2 % 2 == 0:
    if cell3 % 2 == 0 and cell4 % 2 == 0:
        val = 'YES'
    elif cell3 % 2 != 0 and cell4 % 2 != 0:
        val = 'YES'
    else:
        val = 'NO'
elif cell1 % 2 != 0 and cell2 % 2 != 0:
    if cell3 % 2 == 0 and cell4 % 2 == 0:
        val = 'YES'
    elif cell3 % 2 != 0 and cell4 % 2 != 0:
        val = 'YES'
    else:
        val = 'NO'
elif cell1 % 2 == 0 and cell2 % 2 != 0:
    if cell3 % 2 == 0 and cell4 % 2 != 0:
        val = 'YES'
    elif cell3 % 2 != 0 and cell4 % 2 == 0:
        val = 'YES'
    else:
        val = 'NO'
elif cell1 % 2 != 0 and cell2 % 2 == 0:
    if cell3 % 2 == 0 and cell4 % 2 != 0:
        val = 'YES'
    elif cell3 % 2 != 0 and cell4 % 2 == 0:
        val = 'YES'
    else:
        val = 'NO'

print(val)
