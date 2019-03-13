from utils import timed

@timed
def sort(numbers: list) -> list:
    for i in range(len(numbers)):
        x = numbers[i] # take our number out of its place
        j = i - 1 # cursor to track "back" through the numbers we've sorted
        while j >= 0 and numbers[j] > x:
            # move the sorted numbers into the next slot
            numbers[j + 1] = numbers[j]
            j -= 1
        # until we find a slot to insert our value in sorted order
        numbers[j + 1] = x
    return numbers