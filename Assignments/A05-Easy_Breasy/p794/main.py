class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X = 0
        O = 0
        for r in range(3):
            for c in range(3):
                if board[r][c] == "X":
                    X += 1
                elif board[r][c] == "O":
                    O += 1
        
        if O > X or O < X - 1:
            return False


        winner_X = False
        winner_O = False
        for r in range(3):
            if board[r] == "XXX":
                winner_X = True
            elif board[r] == "OOO":
                winner_O = True

            if board[0][r] == board[1][r] == board[2][r] == "X":
                winner_X = True
            
            elif board[0][r] == board[1][r] == board[2][r] == "O":
                winner_O = True

        if board[0][0] == board[1][1] == board[2][2] == "X":
            winner_X = True

        elif board[0][0] == board[1][1] == board[2][2] == "O":
            winner_O = True

        if board[0][2] == board[1][1] == board[2][0] == "X":
            winner_X = True

        elif board[0][2] == board[1][1] == board[2][0] == "O":
            winner_O = True


            
        if winner_X == True and winner_O == True:
            return False

        if winner_X == True and X == O:
            return False
        
        if winner_O == True and O < X:
            return False

     
        return True
