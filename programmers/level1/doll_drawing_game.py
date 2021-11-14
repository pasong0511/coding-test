#2021-11-15
def solution(board, moves):
    answer = []
    basket = []
    for i in range(len(moves)):     #moves에 있는 값을 기준으로 열 찾기
        pick = moves.pop(0)
        for x in range(0, len(board)):  #행은 어차피 0부터 배열 끝까지 돌기
            if board[x][pick-1] != 0:
                basket.append(board[x][pick-1])
                board[x][pick-1] = 0    #이미 뽑은 인형 자리는 0 초기화           
                break
        if len(basket) >= 2 and basket[-1] == basket[-2] :   # 동일하면 터뜨리기
            answer.append(basket.pop())
            answer.append(basket.pop())
    print(basket)
    return len(answer)