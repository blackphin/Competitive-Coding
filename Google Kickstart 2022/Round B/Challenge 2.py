import math


def area(radius):
    return math.pi * radius * radius


t = int(input())

for x in range(t):
    r, a, b = list(map(int, (input().split())))
    rad = r
    ans = area(rad)
    while rad > 0:
        rad = rad * a
        if rad > 0:
            ans += area(rad)

        rad = rad // b
        if rad > 0:
            ans += area(rad)

    print(f"Case #{x+1}: " + "%.6f" % ans)
