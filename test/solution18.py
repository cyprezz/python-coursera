n = int(input())

hours = n // 60 // 60
finalHours = hours - 24 * (hours // 24)
minutes = n // 60

finalMinutes = minutes - 60 * hours
seconds = n - minutes * 60
restMinutes = finalMinutes // 10
restSeconds = seconds // 10


print(finalHours, ':', '0' * 0 ** restMinutes,
      finalMinutes, ':', '0' * 0 ** restSeconds, seconds, sep='')
