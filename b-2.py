row = input("行数を入力してください:")
column = input("列数を入力してください:")

row = int(row)
column = int(column)

for i in range(1, row + 1):
    for i_2 in range(1, column + 1):
        print(i * i_2, end="")
        if i_2 % column == 0:
            print()
