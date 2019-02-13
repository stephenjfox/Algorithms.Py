def sort(numbers: list) -> list:

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers