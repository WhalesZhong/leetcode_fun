# coding: utf-8


def longest_substring_without_repeating_characters(s):
    """

    :param s:
    :return:
    """
    choice_part_start_idx = 0
    max_length = 0
    choice_part = {}
    length = 0
    for idx, w in enumerate(s):
        # 如果存在而且索引是在当前选中区间内,则不再计入
        same_w_idx = choice_part.get(w)
        if same_w_idx is None or same_w_idx < choice_part_start_idx:
            choice_part[w] = idx
            length += 1
            continue

        # 遇到已存在相同的字符,则选择字段索引往后移一位继续选择
        if max_length < length:
            max_length = length

        choice_part_start_idx = same_w_idx + 1
        length = idx - same_w_idx
        choice_part[w] = idx

    return length if  max_length < length else max_length


