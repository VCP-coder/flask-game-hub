import random
import copy

class Sudoku:
    def __init__(self):
        self.solution = self.generate_solution()
        self.puzzle = self.make_puzzle(self.solution)
        self.original = copy.deepcopy(self.puzzle)
        self.solved = False

    def generate_solution(self):
        # Simple backtracking Sudoku fill (not the fastest, but works)
        def fill(board, row=0, col=0):
            if row == 9:
                return True
            if col == 9:
                return fill(board, row+1, 0)
            numbers = list(range(1,10))
            random.shuffle(numbers)
            for num in numbers:
                if self.is_safe(board, row, col, num):
                    board[row][col] = num
                    if fill(board, row, col+1):
                        return True
                    board[row][col] = 0
            return False
        board = [[0]*9 for _ in range(9)]
        fill(board)
        return board

    def is_safe(self, board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        boxr, boxc = 3*(row//3), 3*(col//3)
        for r in range(boxr, boxr+3):
            for c in range(boxc, boxc+3):
                if board[r][c]==num:
                    return False
        return True

    def make_puzzle(self, sol, remove=45):
        puz = copy.deepcopy(sol)
        count = 0
        while count < remove:
            r = random.randint(0,8)
            c = random.randint(0,8)
            if puz[r][c]!=0:
                puz[r][c]=0
                count += 1
        return puz

    def move(self, r, c, num):
        if self.original[r][c]!=0:
            return False, "Cannot edit this cell."
        if num<1 or num>9:
            return False, "Invalid number."
        self.puzzle[r][c] = num
        self.solved = self.puzzle == self.solution
        return True, "Move registered."

    def get_state(self):
        return {"puzzle": self.puzzle, "original": self.original, "solved": self.solved}
