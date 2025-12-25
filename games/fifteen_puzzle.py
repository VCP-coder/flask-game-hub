import random

class FifteenPuzzle:
    def __init__(self):
        self.board = self.shuffle()
        self.moves = 0

    def shuffle(self):
        nums = list(range(16))
        while True:
            random.shuffle(nums)
            if self.is_solvable(nums):
                break
        return [nums[i:i+4] for i in range(0, 16, 4)]

    def is_solvable(self, nums):
        inv = 0
        for i in range(16):
            for j in range(i+1, 16):
                if nums[i] and nums[j] and nums[i] > nums[j]:
                    inv += 1
        row = nums.index(0) // 4
        return (inv + row) % 2 == 0

    def find_blank(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j]==0:
                    return i,j

    def move(self, r, c):
        br, bc = self.find_blank()
        if abs(br-r)+abs(bc-c)==1:
            self.board[br][bc], self.board[r][c] = self.board[r][c], self.board[br][bc]
            self.moves += 1
            return True, "Moved"
        return False, "Invalid move"

    def is_solved(self):
        goal = list(range(1,16))+[0]
        flat = [n for row in self.board for n in row]
        return flat==goal

    def get_state(self):
        return {"board": self.board, "moves": self.moves, "solved": self.is_solved()}
