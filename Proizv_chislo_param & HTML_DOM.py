def test_(*args):
    print(*args)

test_('a', 25, 58.365, 'MB', True)

print('-------------------------------------')

def summa(n):
    if n == 0:
        return 1
    else:
        return n * summa(n - 1)

print(summa(7))
