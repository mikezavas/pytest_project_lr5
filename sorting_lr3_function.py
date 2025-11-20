import math


# 1
def bubble_sort(mas):
    """
    Пузырьковая сортировка - O(n²)
    :param mas: Список интов
    :return: Отсортированный список интов и кол-во итераций
    """
    if len(mas) <= 1:
        return mas, 0

    n = len(mas)
    count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                count += 1
    return mas, count


# 2
def selection_sort(nums):
    """
    Сортировка выборкой - O(n²)
    :param nums: список интов
    :return: отсортированный список и количество итераций
    """
    if len(nums) <= 1:
        return nums, 0

    k = 0
    for i in range(len(nums)):
        index = i
        for j in range(i + 1, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
        k += 1
    return nums, k


# 3
def insertion_sort(nums):
    """
    Сортировка вставками - O(n²) в худшем, O(n) в лучшем
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums, 0

    k = 0
    for i in range(1, len(nums)):
        elem = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > elem:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = elem
        k += 1
    return nums, k


# 4
def heapify(nums, heap_size, root_index):
    largest = root_index
    l_child = (2 * root_index) + 1
    r_child = (2 * root_index) + 2
    if l_child < heap_size and nums[l_child] > nums[largest]:
        largest = l_child
    if r_child < heap_size and nums[r_child] > nums[largest]:
        largest = r_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    """
    Пирамидальная сортировка - O(n log n)
    :param nums: список интов
    :return: отсортированный список и количество итераций
    """
    if len(nums) <= 1:
        return nums, 0

    n = len(nums)
    k = 0
    for i in range(n, -1, -1):
        heapify(nums, n, i)
        k += 1

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        k += 1
    return nums, k


# 5
def merge_two_list(a, b):
    """
    Сортировка слиянием - O(n log n)
    :param a: первый отсортированный список
    :param b: второй отсортированный список
    :return: слияние двух отсортированных списков
    """
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    """

    :param s: список интов
    :return: список отсортированный и количество итераций
    """
    if len(s) <= 1:
        return s, 0

    middle = len(s) // 2
    left = s[:middle]
    right = s[middle:]

    left_sorted, l_count = merge_sort(left)
    right_sorted, r_count = merge_sort(right)

    result = merge_two_list(left_sorted, right_sorted)
    k = 1 + l_count + r_count

    return result, k

# 6
def quick_sort(s):
    """
    Быстрая сортировка - O(n log n) в среднем, O(n²) в худшем
    :param s: список интов
    :return: отсортированный список
    """
    if len(s) <= 1:
        return s, 0

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    left_sorted, left_count = quick_sort(left)
    right_sorted, right_count = quick_sort(right)

    k = 1 + left_count + right_count
    result = left_sorted + middle + right_sorted

    return result, k


if __name__ == "__main__":
    s = list(map(int, input().split()))
