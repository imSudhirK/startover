# Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150


def findMinArrowShotsV1(points):
    lp = len(points)
    if not lp: return 0
    points.sort(key = lambda p: p[0])
    indx, count = 0, 0
    while indx < lp:
        if indx == lp - 1:
            count += 1
        elif points[indx][1] < points[indx + 1][0]:
            count += 1
        else:
            new_point = [points[indx + 1][0], min(points[indx][1], points[indx + 1][1])]
            points[indx + 1] = new_point
        indx += 1
    return count

def findMinArrowShotsV2(points):
    lp = len(points)
    if not lp: return 0
    points.sort(key = lambda p: p[1])
    count, arrow_x = 1, points[0][1]
    for start, end in points[1:]:
        if start > arrow_x:
            arrow_x = end
            count += 1
    return count

print('findMinArrowShotsV1\t', findMinArrowShotsV1([[10,16],[2,8],[1,6],[7,12]]))
print('findMinArrowShotsV1\t', findMinArrowShotsV2([[10,16],[2,8],[1,6],[7,12]]))