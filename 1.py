# Дан массив целых чисел х длиной N. Массив упорядочен по возрастанию. Написать функцию, которая из этого массива
# получит массив квадратов чисел, упорядоченный по возрастанию.

# https://www.youtube.com/live/tfvm2k5c9JI?si=z804PGlYg12jDF9v&t=1260

# https://leetcode.com/problems/squares-of-a-sorted-array

def main(arr):
    left, right = 0, len(arr) - 1
    res = []
    while left <= right:
        if arr[left] ** 2 > arr[right] ** 2:
            res.append(arr[left] ** 2)
            left += 1
        else:
            res.append(arr[right] ** 2)
            right -= 1
    return res[::-1]


test_lst = [-100, -62, -4, 13, 99]
print(main(test_lst))

