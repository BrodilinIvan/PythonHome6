"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def payroll_preparation():
    try:
        script_name, total_time, rate_hours, bonus = argv
        total_time = int(total_time)
        rate_hours = float(rate_hours)
        bonus = float(bonus)
        print(f'Заработная плата сотрудника: '
              f'{total_time * rate_hours + bonus}')
    except ValueError:
        print('Введено некорректное значение!')


payroll_preparation()
