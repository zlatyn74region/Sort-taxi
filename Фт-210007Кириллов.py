from library.Lab2 import num2text

def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
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

kils = list()
for i in range(amount_emps):
    kils.append(input_int(f'Введите количество километров до дома для {i+1} сотрудника: ', 1))

tax = list()
for i in range(amount_emps):
    tax.append(input_int(f'Введите стоимость тарифа в рублях за проезд одного километра для {i+1} машины такси: ', 1))

final = [0 for i in range(amount_emps)]

sum = 0
for i in range(amount_emps):
    sum += min(kils) * max(tax)
    final[kils.index(min(kils))] = tax.index(max(tax))
    kils[kils.index(min(kils))] = max(kils)+1
    tax[tax.index(max(tax))] = 0

for i in range(amount_emps):
    print(f'Для {i+1} сотрудника {final[i]+1} такси ')

print('Общая сумма за просчитанный вариант в числовом виде:', sum)
print('Общая сумма за просчитанный вариант в словесном виде:', num2text(sum, ((u'рубль', u'рубля', u'рублей'), 'm')).capitalize())