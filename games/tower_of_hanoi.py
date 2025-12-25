class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.pegs = {
            'source': list(range(num_disks, 0, -1)),
            'middle': [],
            'destination': []
        }

    def move_disk(self, from_peg, to_peg):
        # Validate move
        if not self.pegs[from_peg]:
            return False, "Source peg is empty"
        moving_disk = self.pegs[from_peg][-1]
        if self.pegs[to_peg] and self.pegs[to_peg][-1] < moving_disk:
            return False, "Cannot place larger disk on smaller disk"
        self.pegs[from_peg].pop()
        self.pegs[to_peg].append(moving_disk)
        return True, "Move successful"

    def is_solved(self):
        return len(self.pegs['destination']) == self.num_disks

    def get_state(self):
        return self.pegs
