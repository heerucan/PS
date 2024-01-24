n = int(input());

result = 0
while n > 0:
    # 최소 봉지니까 5로 먼저 나눠떨어지는지 체크
    if n%5==0:
        result += n//5
        break
    # 아닌 경우 [3봉지]로 배달
    n -= 3
    result += 1 # 횟수+=1
    # 만약, 배달할 kg이 1,2면 -> 남아버린 것 -> -1반환
    if 0 < n < 3:
        result = -1
        break

print(result)