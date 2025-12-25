import random

class Minesweeper:
    def __init__(self, rows=9, cols=9, mines=10):
        self.rows, self.cols, self.mines = rows, cols, mines
        self.board = [[0]*cols for _ in range(rows)]
        self.revealed = [[False]*cols for _ in range(rows)]
        self.flagged = [[False]*cols for _ in range(rows)]
        self.loss = False
        self.win = False
        self._place_mines()
        self._compute_numbers()

    def _place_mines(self):
        placed = 0
        while placed < self.mines:
            r, c = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            if self.board[r][c] != -1:
                self.board[r][c] = -1
                placed += 1

    def _compute_numbers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]==-1:
                    continue
                count = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        nr, nc = i+dr, j+dc
                        if 0<=nr<self.rows and 0<=nc<self.cols and self.board[nr][nc]==-1:
                            count += 1
                self.board[i][j]=count

    def click(self, r, c, button):
        if self.loss or self.win or self.flagged[r][c]:
            return True, "No action."
        if button=='right':
            self.flagged[r][c] = not self.flagged[r][c]
            return True,"Flag toggled."
        if self.board[r][c]==-1:
            self.revealed[r][c]=True
            self.loss = True
            return True,"Boom!"
        self._reveal(r,c)
        self.win = self._check_win()
        return True, "Revealed."

    def _reveal(self, r, c):
        if not (0<=r<self.rows and 0<=c<self.cols): return
        if self.revealed[r][c] or self.flagged[r][c]: return
        self.revealed[r][c]=True
        if self.board[r][c]==0:
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr!=0 or dc!=0:
                        self._reveal(r+dr, c+dc)

    def _check_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]!=-1 and not self.revealed[i][j]:
                    return False
        return True

    def get_state(self):
        return {
            "board": self.board,
            "revealed": self.revealed,
            "flagged": self.flagged,
            "win": self.win,
            "loss": self.loss
        }
