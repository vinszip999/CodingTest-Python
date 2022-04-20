# <의좋은 형제>
import math

user_input = input()
arr = user_input.split(' ')
num = input()
jw = int(arr[0])
sw = int(arr[1])
temp = 0
for a in range(1, int(num) + 1):
    if a % 2 == 1:
        temp = math.ceil(jw / 2)
        jw -= temp
        sw += temp
    else:
        temp = math.ceil(sw / 2)
        sw -= temp
        jw += temp
print(jw, sw)
