class ConnectFour:
    def __init__(self):
        self.board = [[0]*7 for _ in range(6)]
        self.turn = 1
        self.winner = 0

    def move(self, col):
        if self.winner or col<0 or col>6:
            return False, "Invalid."
        for row in range(5, -1, -1):
            if self.board[row][col]==0:
                self.board[row][col]=self.turn
                if self.check_win(row, col):
                    self.winner = self.turn
                else:
                    self.turn = 1 if self.turn==2 else 2
                return True, "Move registered."
        return False,"Column filled."

    def check_win(self, r, c):
        b, t = self.board, self.turn
        for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]:
            count = 1
            for d in [1,-1]:
                nr, nc = r, c
                while True:
                    nr += dr*d; nc += dc*d
                    if 0<=nr<6 and 0<=nc<7 and b[nr][nc]==t:
                        count+=1
                    else:
                        break
            if count>=4:
                return True
        return False

    def get_state(self):
        return {"board": self.board, "turn": self.turn, "winner": self.winner}
