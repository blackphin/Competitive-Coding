t = int(input())

for z in range(t):
    list1 = []
    l2 = []
    last = 0
    tmp = 0
    ans = 0
    n = int(input())
    list1 = str(input()).split()
    l2 = [int(string) for string in list1]
    ans = 1
    if l2[0] <= l2[len(l2) - 1]:
        last = l2.pop(0)
    elif l2[0] > l2[len(l2) - 1]:
        last = l2.pop(len(l2) - 1)

    for x in range(len(l2)):
        length = len(l2)

        if length == 1:
            if l2[0] >= last:
                ans += 1
        else:
            if l2[0] <= l2[len(l2) - 1]:
                tmp = l2.pop(0)
                if tmp >= last:
                    last = tmp
                    ans += 1

            elif l2[0] > l2[len(l2) - 1]:
                tmp = l2.pop(len(l2) - 1)
                if tmp >= last:
                    last = tmp
                    ans += 1
    print(f"Case #{z+1}: {ans}")
