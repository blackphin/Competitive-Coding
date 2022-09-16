t = int(input())

for x in range(t):
    list_i = []
    list_x = []
    l1 = []
    ans = 0
    n, p = list(map(int, (input().split())))
    for y in range(n):
        list_i = str(input()).split()
        list_x = [int(string) for string in l1]
        l1.append(list_x)

    # tmp = min(l1[0])
    # l1[0].remove(tmp)
    # l1[0].insert(0, tmp)
    # ans += tmp

    for z in range(n - 1):
        if (l1[z])[p - 1] == (s for s in l1[z + 1]):
            l1[z + 1].sort(reverse=True)


def getAns(t: int, n: int, p: int, arr: list):
    ans = 0
    ls, rs = 0, 0

    l, r = 0, 0

    for i in range(n):
        mx = max(arr[i])
        mn = min(arr[i])

        nr = min(abs(ls - mn) + mx - mn + l, abs(rs - mn) + mx - mn + r)
        nl = min(abs(ls - mx) + mx - mn + l, abs(rs - mx) + mx - mn + r)
        r = nr
        l = nl
        ls = mn
        rs = mx
    ans = min(l, r)

    print("Case #{}: {}".format(t, ans))


ts = int(input())
for t in range(ts):
    n, p = [int(i) for i in input().split(" ")]
    arr = [[int(i) for i in input().split(" ")] for i in range(n)]
    getAns(t + 1, n, p, arr)
