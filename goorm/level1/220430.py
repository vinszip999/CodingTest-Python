# <타일 장식물>
user_input = input()
num = int(user_input)
arr = [0, 1]
for a in range(num - 1):
    arr.append(arr[a] + arr[a + 1])
answer = 4 * arr[num] + 2 * arr[num - 1]
print(answer)
