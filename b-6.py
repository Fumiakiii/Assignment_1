import random


def random_number(n, m):
    for i in range(1, m + 1):
        if i == m:
            print(random.randint(1, n), end="")
        else:
            print(random.randint(1, n), end=", ")


number_of_faces = int(input("サイコロの面の数は?:"))
number_of_rolls = int(input("何回振りますか?:"))

random_number(number_of_faces, number_of_rolls)
