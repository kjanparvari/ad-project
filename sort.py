from graph import Edge


def insertion_sort(lst: list):
    for i in range(1, len(lst)):
        # print(f"progress: {round((i / len(lst) * 100), 2)} %")
        key = lst[i].copy()
        j = i - 1
        while j >= 0 and key.score < lst[j].score:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def bubble_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j].score > lst[j + 1].score:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def merge_sort(lst: list) -> list:
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].score < right_half[j].score:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst


def partition(lst: list, low: int, high: int) -> int:
    i = (low - 1)  # index of smaller element
    pivot = lst[high].copy()  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if lst[j].score <= pivot.score:
            # increment index of smaller element
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort_recursive(lst: list, low: int, high: int):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    if len(lst) == 1:
        return lst
    if low < high:
        pi = partition(lst, low, high)
        quick_sort_recursive(lst, low, pi - 1)
        quick_sort_recursive(lst, pi + 1, high)


def quick_sort(lst: list) -> list:
    quick_sort_recursive(lst, 0, len(lst) - 1)
    return lst
