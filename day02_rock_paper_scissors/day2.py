def calculate_score(elf, me):
    score = 3 * (me == elf) + 6 * (me == elf + 1 or me == elf - 2)
    return me + score


def get_my_shape(elf, me):
    my_shape = (points[elf] + (me == "Z") - (me == "X")) % 3
    return 3 if my_shape == 0 else my_shape


points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
total_score_pt1 = 0
total_score_pt2 = 0

for line in open("input.txt").readlines():
    elf, me = line.split()
    total_score_pt1 += calculate_score(points[elf], points[me])
    my_shape = get_my_shape(elf, me)
    total_score_pt2 += calculate_score(points[elf], my_shape)

print(total_score_pt1)  # 13565
print(total_score_pt2)  # 12424
