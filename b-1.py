numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    for i_2 in numbers:
        result = i * i_2
        print(result, end=" ")
        if i_2 % 9 == 0:
            print("")
