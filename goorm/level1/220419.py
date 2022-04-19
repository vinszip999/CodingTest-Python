# <앵무새 꼬꼬>
ex_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
n = int(input())
list1 = []
answer = ""
for i in range(n):
    list1.append(input())
for j in range(n):
    s = list1[j]
    answer = ""
    for k in range(len(s)):
        if s[k] in ex_list:
            answer += s[k]
    if (len(answer) == 0):
        answer = "???"
    print(answer)
