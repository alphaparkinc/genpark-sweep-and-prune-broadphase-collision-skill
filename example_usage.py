from client import SweepAndPrune

sap = SweepAndPrune()
boxes = [
    SweepAndPrune.AABB("hero", 0, 10, 0, 10),
    SweepAndPrune.AABB("enemy", 8, 18, 5, 15),
    SweepAndPrune.AABB("tree", 50, 60, 50, 60)
]

candidates = sap.find_potential_collisions(boxes)
print("Candidate collision pairs:", candidates)
