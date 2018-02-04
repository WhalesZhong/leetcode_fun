# coding: utf-8


d2a = { '1': '',    '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv', '9': 'wxyz',
        '0': ' '}


def letter_combinations_of_a_phone_number(digits):
    """

    :param digits:
    :return:
    """
    ans = [''] if digits else []
    for d in digits:
        ans = [r + e for e in d2a[d] for r in ans]
    return ans
