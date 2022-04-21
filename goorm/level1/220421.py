# <정사각형의 개수>
user_input = input()
num = int(user_input)
total = 0
for a in range(1, num + 1):
	total += a * a
print(total)
