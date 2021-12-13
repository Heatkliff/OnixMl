def sort_by_second_subelement(main_list):
    new_list = sorted(main_list, key=lambda sublist: sublist[1])
    return new_list


def dict_by_second_subelement(main_list):
    new_dict = {elem[1]: elem for elem in main_list}
    return new_dict


def reverse_sort_dict(main_dict):
    sorted_keys = sorted(main_dict, reverse=True)
    new_dict = {key: main_dict[key] for key in sorted_keys}
    return new_dict


def set_by_dict_values(main_dict):
    new_set = set([value for sublist in main_dict.values() for value in sublist])
    return new_set


def str_by_set(main_set):
    return ''.join(map(str, main_set))


if __name__ == "__main__":
    input_list = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
    sorted_list = sort_by_second_subelement(input_list)
    print(sorted_list)
    dict_by_list = dict_by_second_subelement(sorted_list)
    print(dict_by_list)
    reversed_dict = reverse_sort_dict(dict_by_list)
    print(reversed_dict)
    set_by_dict = set_by_dict_values(reversed_dict)
    print(set_by_dict)
    result_str = str_by_set(set_by_dict)
    print(result_str)
