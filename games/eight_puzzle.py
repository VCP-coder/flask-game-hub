import random

class EightPuzzle:
    def __init__(self):
        self.board = self.random_board()
        self.moves = 0

    def random_board(self):
        nums = list(range(9))
        while True:
            random.shuffle(nums)
            if self.is_solvable(nums):
                return [nums[i:i+3] for i in range(0,9,3)]

    def is_solvable(self, flat):
        inv = 0
        for i in range(9):
            for j in range(i+1,9):
                if flat[i] and flat[j] and flat[i] > flat[j]:
                    inv += 1
        return inv % 2 == 0

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def move(self, r, c):
        br, bc = self.find_blank()
        if abs(br - r) + abs(bc - c) == 1:
            self.board[br][bc], self.board[r][c] = self.board[r][c], self.board[br][bc]
            self.moves += 1
            return True, "Moved"
        return False, "Invalid move"

    def is_solved(self):
        goal = [1,2,3,4,5,6,7,8,0]
        return [num for row in self.board for num in row] == goal

    def get_state(self):
        return {"board": self.board, "moves": self.moves, "solved": self.is_solved()}
