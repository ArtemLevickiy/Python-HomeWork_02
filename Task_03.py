# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

Indexs = list(range(5))
Indexs[0] = int(input('Введите 1-й ИНДЕКС: '))
Indexs[1] = int(input('Введите 2-й ИНДЕКС: '))
Indexs[2] = int(input('Введите 3-й ИНДЕКС: '))
Indexs[3] = int(input('Введите 4-й ИНДЕКС: '))
Indexs[4] = int(input('Введите 5-й ИНДЕКС: '))

N = int(input('Введите число: '))
Numbers = list(range(-N,N+1))
print(Numbers)
print(f'Произведение элементов на индексах {Indexs} = \
{Numbers[Indexs[0]]} * {Numbers[Indexs[1]]} * {Numbers[Indexs[2]]} * {Numbers[Indexs[3]]} * {Numbers[Indexs[4]]} = \
{Numbers[Indexs[0]] * Numbers[Indexs[1]] * Numbers[Indexs[2]] * Numbers[Indexs[3]] * Numbers[Indexs[4]]}')
