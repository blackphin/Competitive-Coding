T = int(input())
for x in range(T):
    n = int(input())
    g = int(input())
    l1 = str(input()).split()
    for g in range(len(l1)):
        l1[g] = int(l1[g])
    l1.sort()
    answer = 0
    for y in range(n):
        answer += l1[y]
    print(answer)
    l1 = []
