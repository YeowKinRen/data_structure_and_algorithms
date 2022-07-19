import matplotlib.pyplot as plt

"""
start from the leftmost point / minimum x coordinate value
wrapping points in counterclockwise direction
"""


# class Point:
#     def __init__(self, x, y):
#         self[0] = x
#         self[1] = y
# 

# def Left_index(points):
#     '''
#     Finding the left most point
#     '''
#     minn = 0
#     for i in range(1, len(points)):
#         if points[i][0] < points[minn][0]:
#             minn = i
#         elif points[i][0] == points[minn][0]:
#             if points[i][1] > points[minn][1]:
#                 minn = i
#     return minn


# def orientation(p, q, r):
#     '''
#     To find orientation of ordered triplet (p, q, r).
#     The function returns following values
#     0 --> p, q and r are collinear
#     1 --> Clockwise
#     2 --> Counterclockwise
#     '''
#     val = (q[1] - p[1]) * (r[0] - q[0]) - \
#           (q[0] - p[0]) * (r[1] - q[1])
#
#     if val == 0:
#         return 0
#     elif val > 0:
#         return 1
#     else:
#         return 2


def convexHull(points):
    n = len(points)

    if n < 3:  # There must be at least 3 points
        return

    points_sorted = sorted(points)
    # print(points_sorted)
    l = points.index(points_sorted[0])
    # l = Left_index(points)

    hull = []

    '''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again. This loop runs O(h)
    times where h is number of points in result or output.
    '''
    p = l
    q = 0
    while True:
        hull.append(p)  # Add current point to result

        '''
        Search for a point 'q' such that orientation(p, q,
        x) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
        q = (p + 1) % n

        for i in range(n):

            # If i is more counterclockwise than current q, then update q
            if (((points[i][1] - points[p][1]) * (points[q][0] - points[i][0])) -
            ((points[i][0] - points[p][0]) * (points[q][1] - points[i][1]))) < 0:
                """slope of the line segment p to i to q
                σ = (y2 - y1)/(x2 - x1) ;τ = (y3 - y2)/(x3 - x2); σ / τ = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)"""
                q = i
        p = q  # q is the most counterclockwise with respect to p

        if p == l:  # While we don't come to first point
            hull.append(p)
            plt.plot(*zip(*[points[x] for x in hull]))
            break

    # Print Result
    for each in hull:
        print(points[each][0], points[each][1])
    return hull

if __name__ == '__main__':

    # Driver Code
    points = [(0, 3), (1, 1), (2, 2), (4, 4),
              (0, 0), (1, 2), (3, 1), (3, 3)]

    # points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    plt.scatter(*zip(*points))
    plt.pause(0.05)

    hull = convexHull(points)
    print(hull)

    # plt.plot(x, y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
    plt.show()
