import random


def random_number(n):
    print(random.randint(1, n), end=", ")


number_of_faces = int(input("サイコロの面の数は?:"))
number_of_rolls = input("何回振りますか?:")

for i in range(1, int(number_of_rolls) + 1):
    random_number(number_of_faces)
