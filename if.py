x = 38

print('дратути')
if x < 0:
    print('Меньше нуля')
print('дотвиданья')

# примеры
a, b = 10, 5
if a > b:
    print('a > b')

# можно сравнивать числа, строки, списки...
if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')

if '34' > '123': # строки сравнениваются только посимвольно (сравнение начинается с первых сравниваемых символов)
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]: # в списках сравниваются элементы (сравнение начинается с первых сравниваемых элементов)
    print('успех')

# нельзя сравнивать - разные типы
if '6' > 5:
    print('успех')

if [5, 6] > 5:
    print('успех')

# но
if '6' != 5:
    print('успех')
