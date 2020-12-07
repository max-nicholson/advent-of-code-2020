import os

def product_of_two_numbers_summing_to(target, numbers):
    for i, num in enumerate(numbers):
        if num > target:
            return "No Solution"

        for j in range(len(numbers) - 1, i + 1, -1):
            total = num + numbers[j]
            if total == 2020:
                return num * numbers[j]
            elif total < 2020:
                break
    else:
        return "No Solution"


def product_of_three_numbers_summing_to(target, numbers):
    for i in range(len(numbers) - 2):
        first = numbers[i]
        if first > target:
            return "No Solution"

        for j in range(len(numbers) - 1, i + 1, -1):
            second = numbers[j]

            if first + second > target:
                continue

            for k in range(i + 1, j):
                third = numbers[k]

                total = first + second + third

                if total == target:
                    return first * second * third
                elif total > target:
                    break

    return "No Solution"

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        numbers = [int(line.rstrip()) for line in f]

    numbers.sort()
    print(product_of_two_numbers_summing_to(2020, numbers))
    print(product_of_three_numbers_summing_to(2020, numbers))
