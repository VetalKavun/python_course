def mean(mylist):
    if type(mylist) == dict:
        return sum(mylist.values()) / len(mylist)

    return sum(mylist) / len(mylist)

test_list = [1, 2, 3, 4, 5]
print(mean(test_list))

test_list_dict = {"1": 1, "2": 2, "3": 3}
print(mean(test_list_dict))
