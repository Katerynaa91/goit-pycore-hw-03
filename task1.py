"""Завдання 1: Створіть функцію, яка розраховує кількість днів між заданою датою і поточною датою.
"""

from datetime import datetime


def get_days_from_today(str_date: str) -> int:
    """Функція, яка розраховує кількість днів між заданою датою і поточною датою.
    У якості параметра функція приймає рядок.
    Функція повертає ціле число. 
    """

    if isinstance(str_date, str) == False:        
        raise TypeError ('Введене значення має бути рядком')
    else:
        date_from_str = datetime.strptime(str_date, '%Y-%m-%d').date()
        cur_date = datetime.today()
        difference = int(str(cur_date - date_from_str).split()[0])

    return difference

count_from_date_previous = '2024-05-10'
count_from_date_upcoming = '2024-09-10'

print(get_days_from_today(count_from_date_previous))
print(get_days_from_today(count_from_date_upcoming))