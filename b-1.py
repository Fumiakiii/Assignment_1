for i in range(1, 10):
    for i_2 in range(1, 10):
        result = i * i_2
        print(result, end=" ")
        if i_2 % 9 == 0:
            print("")
