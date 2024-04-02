def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)
print_params()
print_params(2, 3)
print_params(b = 25)
print_params(c = [1, 2, 3])

print('----------------------------------------------------')

value_list = (1, 'b', 3.14)
value_dict = {'a': 10, 'b': 'MB', 'c': False}
print_params(*value_list)
print_params(**value_dict)



value_list2 = (15, 'iPhone')
print_params(*value_list2, 42)
