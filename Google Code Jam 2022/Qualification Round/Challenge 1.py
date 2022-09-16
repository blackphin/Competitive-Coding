def row1(z):
    print("+", end="")
    print("-+" * z)


def top(z):
    print("..", end="")
    print("+-" * (z - 1), end="")
    print("+")


def content(z):
    print("|", end="")
    print(".|" * z)
    row1(z)


def initial_content(z):
    print("..|", end="")
    print(".|" * (z - 1))


n = int(input())
column = []
row = []
for x in range(n):
    list1 = str(input()).split()
    column.append(int(list1[0]))
    row.append(int(list1[1]))
    list1 = []


def execute(row2, column2):
    top(row2)
    initial_content(row2)
    row1(row2)
    for y in range(column2 - 1):
        content(row2)


for x in range(n):
    print(f"Case #{x+1}:")
    row3 = row[x]
    column3 = column[x]
    execute(row3, column3)
