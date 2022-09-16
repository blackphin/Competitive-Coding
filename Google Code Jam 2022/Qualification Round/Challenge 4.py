# t = int(input())

# indent +1 everything after for statement for final execution
# for x in range(t):
struct = [0]

# n = int(input())
# f_list = str(input()).split()
# p_list = str(input()).split()

n = 4
f_list = ["60", "20", "40", "50"]
p_list = ["0", "1", "1", "2"]
answers = []

for a in range(n):
    struct.append([a + 1, int(f_list[a]), int(p_list[a]), 0])


print(struct)

count = 0


"""def create():
    global count
    count += 1
    temp = "list" + str(count)
    tmp = globals()[temp] = []
    return tmp"""
while True:
    tmp_list = []
    for x in struct:
        print(x)
        if x == 0:
            print("f")
            continue
        else:

            b = -1
            while True:
                if b == 0 or b == x[2]:
                    print("gg")
                    break
                else:
                    tmp_list.append(x)
                    b = x[2]
        print(tmp_list)

    break
