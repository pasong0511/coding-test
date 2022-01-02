def default_matricx(rows, columns) :
    matricx = []
    num = 0
    for i in range(rows) :
        temp = []
        for j in range(columns) :
            num += 1
            temp.append(num)                    #1부터 채워넣기
        matricx.append(temp)
    return matricx

rows = 6
columns = 8
board = default_matricx(rows, columns)
print(board)