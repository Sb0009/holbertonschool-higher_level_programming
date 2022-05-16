#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    iterators = 0
    if (my_list_1 < my_list_2):
        iterators = len(my_list_1)
    else:
        iterators = len(my_list_2)
    number = 0
    for i in range(iterators):
        try:
            number = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            number = 0
        except IndexError:
            print("Out of range")
            number = 0
        except TypeError:
            print("wrong type")
            number = 0
        finally:
            newList.append(number)
    return newList
