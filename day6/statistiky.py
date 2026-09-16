numbers = [1, 2, 4, 65, 203, 9, 12]


def statistics(nums):
    lowest = min(nums)
    highest = max(nums)
    average = sum(nums) / len(nums)

    nums = sorted(nums)
    if len(nums) % 2 == 1:
        med = nums[len(nums)//2]
    else:
        x = len(nums)//2
        y = x - 1
        med = (nums[x] + nums[y]) / 2

    return {"min": lowest, "max": highest, "prumer": average, "median": med}


print(statistics(numbers))

