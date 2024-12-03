import random


def random_number(n, m):
    results = []
    for _ in range(m):
        results.append(random.randint(1, n))
    return results


number_of_faces = int(input("サイコロの面の数は?:"))
number_of_rolls = int(input("何回振りますか?:"))


rolls = random_number(number_of_faces, number_of_rolls)
print(rolls)
