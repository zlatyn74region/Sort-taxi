# Используем дополнительную библиотеку для 
# преобразования чисел в словесную форму.
from library.Lab2 import num2text


def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
    '''
    Берет на ввод у пользователя число с дальнейшей проверкой.

    Параметры:
    msg - Сообщение подающееся на ввод пользователю.
    min - Минимальное значение на ввод.
    max - Максимальное значение на ввод.

    Возврат:
    Корректно введенное число.
    '''
    while True:
        try:
            num = int(input(msg))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            return num
        except:
            print('Ошибка: нужно ввести число!')


amount_emps = input_int('Введите количество сотрудников: ', 1, 1000)

kiloms = list()
for i in range(amount_emps):
    kiloms.append(input_int(f'Введите количество километров до дома для {i+1} сотрудника: ', 1))

tax = list()
for i in range(amount_emps):
    tax.append(input_int(f'Введите стоимость тарифа в рублях за проезд одного километра для {i+1} машины такси: ', 1))

# Список, в котором каждому сотруднику соотвествует его такси.
final = [0 for i in range(amount_emps)]

# Подсчет суммы и распределение сотрудников по такси.
sum = 0
for i in range(amount_emps):
    sum += min(kiloms) * max(tax)
    final[kiloms.index(min(kiloms))] = tax.index(max(tax))
    kiloms[kiloms.index(min(kiloms))] = max(kiloms)+1
    tax[tax.index(max(tax))] = 0

# Вывод результатов.
for i in range(amount_emps):
    print(f'Для {i+1} сотрудника {final[i]+1} такси ')

print('Общая сумма за просчитанный вариант в числовом виде:', sum)
print('Общая сумма за просчитанный вариант в словесном виде:', num2text(sum, ((u'рубль', u'рубля', u'рублей'), 'm')).capitalize())