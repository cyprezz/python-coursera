v = int(input())
t = int(input())

s = 109
distance = v * t
laps = distance // s
stop = distance - s * laps

print(stop)
