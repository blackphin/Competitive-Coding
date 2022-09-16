t = int(input())
c = []
m = []
y = []
k = []
answer = []
for a in range(t):
    printer1 = str(input()).split()
    printer2 = str(input()).split()
    printer3 = str(input()).split()

    c.extend([int(printer1[0]), int(printer2[0]), int(printer3[0])])
    m.extend([int(printer1[1]), int(printer2[1]), int(printer3[1])])
    y.extend([int(printer1[2]), int(printer2[2]), int(printer3[2])])
    k.extend([int(printer1[3]), int(printer2[3]), int(printer3[3])])

    if len(c) > 3 or len(m) > 3 or len(y) > 3 or len(k) > 3:
        c = [c[0]] + [c[1]] + [c[2]]
        m = [m[3]] + [m[4]] + [m[5]]
        y = [y[6]] + [y[7]] + [y[8]]
        k = [k[9]] + [k[10]] + [k[11]]
    if (min(c) + min(m) + min(y) + min(k)) >= 1000000:
        raw_temp = min(c) + min(m)
        if raw_temp < 1000000:
            raw_temp += min(y)
            if raw_temp < 1000000:
                raw_temp += min(k)
                diff = raw_temp - 1000000
                answer.append(
                    f"{str(min(c))} {str(min(m))} {str(min(y))} {str(min(k)-diff)}"
                )
            else:
                diff = raw_temp - 1000000
                answer.append(f"{str(min(c))} {str(min(m))} {str(min(y)-diff)} {'0'}")
        else:
            diff = raw_temp - 1000000
            answer.append(f"{str(min(c))} {str(min(m)-diff)} {'0'} {'0'}")
    else:
        answer.append("IMPOSSIBLE")
    printer1 = printer2 = printer3 = c = m = y = k = []
for b in range(0, t):
    print(f"Case #{b+1}: {answer[b]}")
