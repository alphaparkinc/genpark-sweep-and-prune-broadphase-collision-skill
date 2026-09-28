"""Sweep-and-Prune Broadphase Collision Engine.
100% Python Standard Library.
"""

class SweepAndPrune:
    """1D axis projection sweep-and-prune broadphase collision algorithm."""
    class AABB:
        def __init__(self, id_val, min_x, max_x, min_y, max_y):
            self.id = id_val
            self.min_x = min_x
            self.max_x = max_x
            self.min_y = min_y
            self.max_y = max_y

    def find_potential_collisions(self, aabbs):
        sorted_boxes = sorted(aabbs, key=lambda b: b.min_x)
        pairs = []
        for i in range(len(sorted_boxes)):
            for j in range(i + 1, len(sorted_boxes)):
                b1 = sorted_boxes[i]
                b2 = sorted_boxes[j]
                if b2.min_x > b1.max_x:
                    break
                if not (b1.max_y < b2.min_y or b1.min_y > b2.max_y):
                    pairs.append((b1.id, b2.id))
        return pairs
