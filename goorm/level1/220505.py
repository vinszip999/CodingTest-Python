# <고장난 컴퓨터>
user_input = input()
user_input2 = input()
arr1 = user_input.split(' ')
arr2 = user_input2.split(' ')
num1 = int(arr1[0])
num2 = int(arr1[1])
arr = []
for i in arr2:
    arr.append(int(i))
cnt = 1
for j in range(num1 - 1):
    if (arr[j + 1] - arr[j]) > num2:
        cnt = 1
    else:
        cnt += 1
print(cnt)
