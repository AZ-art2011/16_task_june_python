# Задача 16. Найти количество указанных чисел в списке из N элементов

count_n = abs(int(input('Укажите число элементов списка: ')))
elements_of_list = [x for x in range(1, count_n + 1)]

x = abs(int(input('Введите число для поиска в списке: ')))
count = 0

for i in elements_of_list:
  if i == x:
      count += 1

if count != 0:
    print(f'Число {x} встречается в этом списке {count} раз')
else:
    print('Такого элемента в этом списке нет')