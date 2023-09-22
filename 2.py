# Дан массив nums, длиной n и число q
# После даются q запросов, каждый запрос это два числа l, r (1 <= l <= r <= n)
# Нужно прибавить к числам nums[l], nums[l + 1], ... , nums[r] единицу
# В конце вывести массив nums

# https://www.youtube.com/watch?v=RBPSMZHjdFQ


def main(nums, q, req_list):
    nums_res = nums.copy()
    pr_start = [0]
    for i in range(len(nums)):
        pr_start.append(pr_start[i] + nums[i])
    for l, r in req_list:
        nums[l] += 1
        if r + 1 < len(nums):
            nums[r + 1] -= 1
    pr_end = [0]
    for j in range(len(nums)):
        pr_end.append(pr_end[j] + nums[j])
    for k in range(len(nums)):
        nums_res[k] += pr_end[k + 1] - pr_start[k + 1]
    return nums_res


lst = [5, 1, 4, 6]
q = 2
reqs = [(0, 2), (1, 3)]

print(main(lst, q, reqs))

