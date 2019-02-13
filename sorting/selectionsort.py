def sort(numbers: list) -> list:
    for i in range(len(numbers) - 1):
        mindex = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[mindex]:
                mindex = j

        if mindex != i:
            numbers[i], numbers[mindex] = numbers[mindex], numbers[i]

    return list