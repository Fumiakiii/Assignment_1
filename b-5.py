def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def max(numbers):
    max_value = numbers[0]
    for i in numbers:
        if i > max_value:
            max_value = i
    return max_value


def min(numbers):
    min_value = numbers[0]
    for i in numbers:
        if i < min_value:
            min_value = i
    return min_value


def ave(numbers):
    total = 0
    for i in numbers:
        total += i
    ave_value = total // len(numbers)
    return ave_value


input_data = input("データを入力してください(スペース区切り) > ")
numbers = [int(i) for i in input_data.split()]

print(f"合計値: {sum(numbers)}")
print(f"最大値: {max(numbers)}")
print(f"最小値: {min(numbers)}")
print(f"平均値: {ave(numbers)}")
