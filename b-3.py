row = input("行数を入力してください:")
column = input("列数を入力してください:")

row = int(row)
column = int(column)

for i in range(1, row + 1):
    for i_2 in range(1, column + 1):
        # print(str(i).rjust(2), "x", str(i_2).rjust(2), "=", str(i * i_2).rjust(2), end="|")
        print(str(i), "x", str(i_2), " = ", str(i * i_2).rjust(2), end="|")
        if i_2 % column == 0:
            print()
