# coding: utf-8


def two_sum(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """
    num_dict = {}
    for idx, num in enumerate(nums):
        if num_dict.get(num):
            num_dict[num].append(idx)
        else:
            num_dict[num] = [idx]

    for num in nums:
        other = target - num
        if num == other:
            if len(num_dict[num]) > 1:
                return num_dict[num][:2]
            else:
                continue
        elif num_dict.get(other):
            return [num_dict[num][0], num_dict[other][0]]
