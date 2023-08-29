#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """divides these component by component 2 lists.

    Args:
        my_list_1 (list): this will be the initial list.
        my_list_2 (list): this will be the following list.
        list_length (int): this will be  the amount of component to divide.

    Returns:
        Returns a brand new list (length = list_length) with all divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list
