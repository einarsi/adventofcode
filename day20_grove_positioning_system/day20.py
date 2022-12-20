# This seemed like an easy task, but I completely underestimated it!
# The test dataset had unique numbers, which made it possible to solve
# (after some tweaking of ob1s) using a simple list of numbers and
# modding new position with length of list.
# However, the real dataset turned out to have non-unique numbers,
# which made it impossible to uniquely identify which number to move.
# The below solution attaches an id to each number (it's original
# position in the list, for convenience) so it can be identified
# whenever we need to.


def find_zero_idx(nums):
    for i in range(len(nums)):
        if nums[i][1] == 0:
            return i


def mix(idx_nums, times=1):
    for _ in range(times):
        for idx in range(len(idx_nums)):
            # Find the next number to move.
            for i in range(len(idx_nums)):
                if idx_nums[i][0] == idx:
                    num = idx_nums[i]
                    break
            # Move all numbers on its lhs to the end of the list,
            # then insert the number into its new position directly
            # by index.
            idx_nums = idx_nums[i + 1 :] + idx_nums[:i]
            idx_nums.insert(num[1] % len(idx_nums), num)
    return idx_nums


nums = [int(line) for line in open("input.txt").readlines()]
idx_nums = list(enumerate(nums))

idx_nums = mix(idx_nums)
z = find_zero_idx(idx_nums)

print(pt1 := sum([idx_nums[(z + n * 1000) % len(idx_nums)][1] for n in (1, 2, 3)]))
# assert pt1 == 5904

key = 811589153
idx_nums = list(enumerate([num * key for num in nums]))
idx_nums = mix(idx_nums, 10)
z = find_zero_idx(idx_nums)

print(pt2 := sum([idx_nums[(z + n * 1000) % len(idx_nums)][1] for n in (1, 2, 3)]))
assert pt2 == 8332585833851
