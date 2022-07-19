from functools import cmp_to_key

import matplotlib.pyplot as plt

p0 = (0, 0)


def compare(p1, p2):
    global p0
    # Find orientation
    o = ((p1[1] - p0[1]) * (p2[0] - p1[0]) -
         (p1[0] - p0[0]) * (p2[1] - p1[1]))
    if o == 0:
        if ((p0[0] - p2[0]) * (p0[0] - p2[0]) + (p0[1] - p2[1]) * (p0[1] - p2[1])) >= \
                ((p0[0] - p1[0]) * (p0[0] - p1[0]) + (p0[1] - p1[1]) * (p0[1] - p1[1])):
            return -1
        else:
            return 1
    else:
        if o < 0:
            return -1
        else:
            return 1


def convexHull(points):
    global p0

    # Find the bottommost point
    n = len(points)
    ymin = points[0][1]
    min = 0
    for i in range(1, n):
        y = points[i][1]

        # Pick the bottom-most or chose the left
        # most point in case of tie
        if ((y < ymin) or
                (ymin == y and points[i][0] < points[min][0])):
            ymin = points[i][1]
            min = i

    # Place the bottom-most point at first position
    points[0], points[min] = points[min], points[0]

    # Sort n-1 points with respect to the first point.
    # A point p1 comes before p2 in sorted output if p2
    # has larger polar angle (in counterclockwise
    # direction) than p1
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))

    # If two or more points make same angle with p0,
    # Remove all but the one that is farthest from p0
    # Remember that, in above sorting, our criteria was
    # to keep the farthest point at the end when more than
    # one points have same angle.
    m = 1  # Initialize size of modified array
    for i in range(1, n):

        # Keep removing i while angle of i and i+1 is same
        # with respect to p0
        while ((i < n - 1) and
               (((points[i][1] - p0[1]) * (points[i + 1][0] - points[i][0])) - (
                       (points[i][0] - p0[0]) * (points[i + 1][1] - points[i][1]))) == 0):
            # (orientation(p0, points[i], points[i + 1]) == 0)):
            i += 1

        points[m] = points[i]
        m += 1  # Update size of modified array

    # If modified array of points has less than 3 points,
    # convex hull is not possible
    if m < 3:
        return

    # Create an empty stack and push first three points
    # to it.
    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])

    # Process remaining n-3 points
    for i in range(3, m):

        # Keep removing top while the angle formed by
        # points next-to-top, top, and points[i] makes
        # a non-left turn
        while ((len(S) > 1) and
               (((S[-1][1] - S[-2][1]) * (points[i][0] - S[-1][0])) -
                ((S[-1][0] - S[-2][0]) * (points[i][1] - S[-1][1]))) != 2):
            S.pop()
        S.append(points[i])

    # Now stack has the output points,
    # print contents of stack
    while S:
        p = S[-1]
        print("(" + str(p[0]) + ", " + str(p[1]) + ")")
        S.pop()


# Driver Code
points = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]
plt.scatter(*zip(*points))
plt.show()
convexHull(points)
