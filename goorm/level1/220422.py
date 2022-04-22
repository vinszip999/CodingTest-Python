# <단어의 개수 세기>
user_input = input()
arr = user_input.split(' ')
count = 0
for i in arr:
    if i != '':
        count += 1
print(count)
