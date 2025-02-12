"""Завдання 3. Розробіть функцію, що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри 
та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та 
перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, 
функція автоматично додає код '+38' (для України). """

import re


def normalize_phone(phone_number: str, country_code: str = '+38') -> str:
    """Параметр функції - номер телефона у форматі рядка.
    За допомогою модуля re функція виокремлює із заданого рядка тільки цифри. 
    Виконується перевірка на відповідність встановленому формату номера телефона (10 цифр не враховуючи код країни).
    Функція повертає відформатований рядок - номер телефона з кодом країни"""

    phone_dgts = ''.join(re.findall(r'\d+', phone_number)) 
    num_format = re.findall('[0][0-9]{9}$', phone_dgts)     
    num_format_with_falses = re.findall('[0][0-9]{9}', phone_dgts)

    if num_format and num_format == num_format_with_falses:
        correct_phone = country_code + ''.join(num_format)
    else: 
        return "Invalid number: " + phone_dgts
    
    return correct_phone


raw_numbers = [
    "38051-1-22-22",
    "38050-111-22-2",
    "38050-111-22-2233333",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "  + 38(050) 111 22 11  \\n "
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
