# <가위바위보>
user_input = input()
list1 = user_input.split(' ')
cnt = [list1.count('1'), list1.count('2'), list1.count('3')]

if cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0:
    print(0)
elif cnt[0] == 5 or cnt[1] == 5 or cnt[2] == 5:
    print(0)
elif cnt[0] == 0:
    print(cnt[2])
elif cnt[1] == 0:
    print(cnt[0])
else:
    print(cnt[1])
