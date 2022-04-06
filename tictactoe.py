board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

turn = "x"

print(board[0])
print(board[1])
print(board[2])

while True:
    # Checks to make sure value typed is allowed for game
    try:
        row = int(input("Row: "))
        col = int(input("Col: "))

        if (row or col) > 2:
            print("Invalid index! Choose again!")
            if row > 2:
                row = int(input("Row: "))
            if col > 2:
                col = int(input("Col:"))
        
        else:
            if turn == "x":
                if board[row][col] == "":
                    board[row][col] = "x"
                    turn = "o"
                    print("Now it is o's turn")
                else:
                    print("Space already taken!")
            elif turn == "o":
                if board[row][col] == "":
                    board[row][col] = "o"
                    turn = "x"
                    print("Now it is x's turn")
                else:
                    print("Space already taken!")
            print(board[0])
            print(board[1])
            print(board[2])

        if (board[0][0] and board[0][1] and board[0][2]) == "x":
            print("x wins!")
            break
        elif (board[0][0] and board[0][1] and board[0][2]) == "o":
            print("o wins!")
            break
        
        elif (board[1][0] and board[1][1] and board[1][2]) == "x":
            print("x wins!")
            break
        elif (board[1][0] and board[1][1] and board[1][2]) == "o":
            print("o wins!")
            break

        elif (board[2][0] and board[2][1] and board[2][2]) == "x":
            print("x wins!")
            break
        elif (board[2][0] and board[2][1] and board[2][2]) == "o":
            print("o wins!")
            break
        elif (board[0][0] and board[1][1] and board[2][2]) == "x":
            print("x wins!")
            break
        elif (board[0][0] and board[1][1] and board[2][2]) == "o":
            print("o wins!")
        elif (board[0][2] and board[1][1] and board[2][0]) == "x":
            print("x wins!")
            break
        elif (board[0][2] and board[1][1] and board[2][0]) == "o":
            print("o wins!")
            break

    except ValueError:
        print("Must be integer! Pick again!")
        row = int(input("Row: "))
        col = int(input("Col: "))