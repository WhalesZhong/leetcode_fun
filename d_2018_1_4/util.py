# coding: utf-8


def get_func_name(word_str):
    """
    >>>from d_2018_1_4.util import get_func_name
    >>>get_func_name("Longest Substring Without Repeating Characters")
    'longest_substring_without_repeating_characters'
    :param word_str:
    :return:
    """
    return "_".join(word_str.lower().split(" "))