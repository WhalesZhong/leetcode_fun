# coding: utf-8


def longest_palindromic_substring(s):
    """

    :param s:
    :return:
    """
    choice_part_start_idx = 0
    is_find = False
    max_length = 0
    choice_part = ""
    for idx, w in enumerate(s):
        choice_part += w
        # 如果下一个字符不符合则移动已选中的区间,记录长度
        if choice_part != choice_part[::-1]:
            length = idx - choice_part_start_idx + 1
            if max_length < length:
                max_length = length
            choice_part = choice_part[1:]
            choice_part_start_idx += 1




        same_w_idx = choice_part.get(w)
        if same_w_idx is None or same_w_idx < choice_part_start_idx:
            choice_part[w] = idx
            continue

        length = idx - same_w_idx + 1
        is_find = True
        if max_length < length:
            max_length = length

        choice_part_start_idx = same_w_idx + 1
        choice_part[w] = idx

    if not is_find:
        return ""
    else:
        return s[choice_part_start_idx-1:choice_part_start_idx-1+max_length]