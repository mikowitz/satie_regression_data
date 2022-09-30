extra_qualities = ["ddd", "dd", "d", "A", "AA", "AAA"]


def qualities_for(size):
    if size % 7 in [2, 3, 6, 0]:
        return ["m", "M"] + extra_qualities
    else:
        return ["P"] + extra_qualities


polarities = ["", "-", "+"]

quartertones = ["", "~", "+"]
