class WaterJug:
    def __init__(self, a=4, b=3, target=2):
        self.capacity = [a, b]
        self.state = [0, 0]  # [jug1, jug2]
        self.target = target
        self.moves = 0

    def get_state(self):
        return {
            "state": self.state.copy(),
            "capacity": self.capacity,
            "target": self.target,
            "solved": self.target in self.state,
            "moves": self.moves
        }

    def fill(self, which):
        self.state[which] = self.capacity[which]
        self.moves += 1
        return True, f"Jug {which+1} filled."

    def empty(self, which):
        self.state[which] = 0
        self.moves += 1
        return True, f"Jug {which+1} emptied."

    def pour(self, from_, to_):
        available = self.capacity[to_] - self.state[to_]
        poured = min(self.state[from_], available)
        self.state[from_] -= poured
        self.state[to_] += poured
        self.moves += 1
        return True, f"Poured {poured} from Jug {from_+1} to Jug {to_+1}."

    def action(self, act, idx=None):
        if act == "fill":
            return self.fill(idx)
        elif act == "empty":
            return self.empty(idx)
        elif act == "pour":
            return self.pour(idx[0], idx[1])
        return False, "Invalid action."
