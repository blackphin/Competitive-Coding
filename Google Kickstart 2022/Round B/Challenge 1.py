t = int(input())

list1 = []


def factors(x):
    global list1
    result = []
    list1 = []
    i = 1

    while i * i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1
    list1 = result


def reverse(num):
    xnum = str(num)
    return int(xnum[::-1])


sum1 = 0
for a in range(t):
    sum1 = 0
    b = int(input())
    factors(b)
    for g in list1:
        if g == reverse(g):
            sum1 += 1
    print(f"Case #{a+1}: {sum1}")
