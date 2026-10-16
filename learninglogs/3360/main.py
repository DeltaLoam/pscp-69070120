"""หั่นขนมปัง"""


def gaps(cuts, size):
    """gaps"""
    edges = [0] + cuts + [size]
    return [b - a for a, b in zip(edges, edges[1:])]


def main():
    """หั่นขนมปัง"""
    w, h = map(int, input().split()[:2])
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    widths = sorted(gaps(xs, w), reverse=True)
    heights = sorted(gaps(ys, h), reverse=True)
    cand = [widths[0] * heights[0]]
    if len(widths) > 1:
        cand.append(widths[1] * heights[0])
    if len(heights) > 1:
        cand.append(widths[0] * heights[1])
    cand.sort(reverse=True)
    print(cand[0], cand[1] if len(cand) > 1 else cand[0])

main()
