class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current = "X"
        self.winner = None
        self.moves = 0

    def make_move(self, pos):
        if self.board[pos] or self.winner:
            return False, "Invalid move"
        self.board[pos] = self.current
        self.moves += 1
        self.winner = self.check_winner()
        msg = f"Player {self.current} moved"
        if self.winner:
            msg = f"Player {self.current} wins!" if self.winner!="Draw" else "It's a draw!"
        else:
            self.current = "O" if self.current == "X" else "X"
        return True, msg

    def check_winner(self):
        b = self.board
        wins = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
        for w in wins:
            if b[w[0]] and b[w[0]]==b[w[1]]==b[w[2]]:
                return b[w[0]]
        if self.moves == 9:
            return "Draw"
        return None

    def get_state(self):
        return {
            "board": self.board,
            "current": self.current,
            "winner": self.winner
        }
