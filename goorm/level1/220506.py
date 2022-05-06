# <막대기>
user_input = int(input())

board = []

for _ in range(user_input):
    temp = int(input())
    board.append(temp)

cnt = 1
maxNum = board[-1]

for i in range(user_input - 1, -1, -1):
    if maxNum < board[i - 1]:
        cnt += 1
        maxNum = max(board[i - 1], board[i])

print(cnt)
