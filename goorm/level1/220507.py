# <뱀이 지나간 자리>
user_input = input()

list1 = user_input.split(" ")

num1 = int(list1[0])
num2 = int(list1[1])

str1 = '#' * num2
str2 = '.' * (num2 - 1) + '#'
str3 = '#' + '.' * (num2 - 1)

road = []
cnt = 0

for a in range(num1):
    if cnt % 2 == 0:
        road.append(str1)
    else:
        if cnt % 4 == 1:
            road.append(str2)
        else:
            road.append(str3)
    cnt += 1

    print(road[a])
