cellH1 = int(input())
cellV1 = int(input())
cellH2 = int(input())
cellV2 = int(input())

if cellV2 <= cellV1:
    val = 'NO'
elif cellH2 > 8 or cellV2 > 8:
    val = 'NO'
elif cellH2 <= 0 or cellH1 <= 0 or cellV1 <= 0 or cellV2 <= 0:
    val = 'NO'
elif (cellH1 % 2 == 0 and cellV1 % 2 == 1) or \
        (cellH1 % 2 == 1 and cellV1 % 2 == 0):
    val = 'NO'
else:
    if abs(cellH2 - cellH1) != abs(cellV2 - cellV1):
        val = 'NO'
    else:
        val = 'YES'

print(val)
