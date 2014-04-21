number_behind = 1
number = 1
temp = 0
sum = 0
while number < 4000000:
    temp = number
    number += number_behind
    number_behind = temp
    if number % 2 == 0: sum += number

print sum