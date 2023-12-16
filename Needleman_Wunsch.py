# Needleman-Wunsch alignment algorithm

penalties = {"sub": -1, "gap": -1, "equ": 0}


def sc(b1, b2):
    if b1 == b2:
        return penalties["equ"]
    else:
        return penalties["sub"]


def sc_gap():
    return penalties["gap"]


def reconstruct(f, g1, g2, i, j):
    if not i and not j:
        yield "", ""

    if j - 1 >= 0:
        if f[i][j] == f[i][j - 1] + sc_gap():
            for align_a, align_b in reconstruct(f, g1, g2, i, j - 1):
                yield align_a + "-", align_b + g2[j - 1]

    if i - 1 >= 0:
        if f[i][j] == f[i - 1][j] + sc_gap():
            for align_a, align_b in reconstruct(f, g1, g2, i - 1, j):
                yield align_a + g1[i - 1], align_b + "-"

    if i - 1 >= 0 and j - 1 >= 0:
        if f[i][j] == f[i - 1][j - 1] + sc(g1[i - 1], g2[j - 1]):
            for align_a, align_b in reconstruct(f, g1, g2, i - 1, j - 1):
                yield align_a + g1[i - 1], align_b + g2[j - 1]


def score(g1, g2):
    f = [[0 for j in range(len(g2) + 1)] for i in range(len(g1) + 1)]

    for i in range(len(g1) + 1):
        f[i][0] = sc_gap() * i

    for j in range(len(g2) + 1):
        f[0][j] = sc_gap() * j

    for i in range(1, len(g1) + 1):
        for j in range(1, len(g2) + 1):
            score_both = f[i - 1][j - 1] + sc(g1[i - 1], g2[j - 1])
            f[i][j] = max(score_both, f[i - 1][j] + sc_gap(), f[i][j - 1] + sc_gap())

    for k in penalties:
        print(k, "penalty", "%2d" % penalties[k])
    print()
    print(g1)
    print(g2)
    print()

    print(" " + "".join("%4c" % c for c in "_" + g2))
    for i, l in enumerate(f):
        print(("_" + g1)[i] + "".join(["%4d" % n for n in l]))
    print()

    for align_a, align_b in reconstruct(f, g1, g2, len(g1), len(g2)):
        print(align_a)
        print(align_b)
        print()


def load_data(filename):
    f = open(filename)
    sequences = [seq for seq in f if len(seq) > 0]
    return sequences


def align():
    sequences = load_data("basestring.dat")
    sequences = [s.strip() for s in sequences]
    for i in range(1, len(sequences)):
        score(sequences[0], sequences[i])


penalties["sub"] = -2
penalties["gap"] = -1
align()
