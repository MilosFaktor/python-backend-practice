with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50")


def read_numbers_from_file(filename):
    with open(filename, "r") as f:
        numbers = f.read().splitlines()
        return [int(num) for num in numbers]


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


nums = read_numbers_from_file("numbers.txt")
avg = calculate_average(nums)
print(f"Average: {avg}")
