# <헷갈리는 작대기>
user_input = input()
count_1 = 0
count_I = 0
count_l = 0
count_a = 0

list1 = list(user_input)
for i in list1:
    if i == '1':
        count_1 += 1
    elif i == 'I':
        count_I += 1
    elif i == 'l':
        count_l += 1
    elif i == '|':
        count_a += 1

print(count_1)
print(count_I)
print(count_l)
print(count_a)

# <더 좋은 풀이>
user_input = input()
cnt = [0, 0, 0, 0]
cnt[0] = user_input.count('1')
cnt[1] = user_input.count('I')
cnt[2] = user_input.count('l')
cnt[3] = user_input.count('|')
for a in cnt:
    print(a)
