n = int(input())

hours = n // 60
mins = n % 60
clockHours = hours // 24
displayHours = hours - 24 * clockHours

print(displayHours, mins)
