# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # True 에 해당하는 요소(item)는 더한다
        if signs[i] is True:  # 참과 거짓을 비교할 땐 == 보단 is를 많이 쓴다
            answer += absolutes[i]
        # False 에 해당하는 요소(item)는 뺀다
        else:
            answer -= absolutes[i]
    return answer
