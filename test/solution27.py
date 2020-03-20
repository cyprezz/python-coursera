cell1 = int(input())
cell2 = int(input())
cell3 = int(input())
cell4 = int(input())

val = ''

if cell1 - cell3 == 1 or cell1 - cell3 == -1 or cell1 - cell3 == 0:
    if cell2 - cell4 == 1 or cell2 - cell4 == -1 or cell2 - cell4 == 0:
        val = 'YES'
    else:
        val = 'NO'
else:
    val = 'NO'
print(val)
