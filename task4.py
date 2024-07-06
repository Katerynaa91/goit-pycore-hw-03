"""Завдання 4. Створити функцію get_upcoming_birthdays, яка повинна повернути список всіх у кого 
день народження вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідні, 
функція повинна переносити дату привітання на наступний робочий день (понеділок). Якщо день народження 
вже минув в цьому році (if birthday_this_year < today), розгляньте дату на наступний рік. 
Вивести зібрані дані у вигляді списку словників з іменами користувачів та датами привітань"""

from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list, days_count:int = 7) -> list:
    """У якості параметра функція приймає список словників, де ключами є ім'я та дата народження у форматі рядка. 
    Функція повертає новий список словників з ключами "ім'я" та "дата привітання" у форматі рядка.
    Якщо дата привітання припадає на вихідний день - дата переноситься на перший робочий день настурного тижня.
    Якщо 7 дній охоплюють 2 роки (наприклад, з 2024.12.27 до 2025.12.02), дата змінюється відровідно.
    """
    date_today = datetime.today().date()
    delta_time = timedelta(days = days_count)
    next_seven_days = datetime.today().date() + delta_time
    birthdays_lst = list()

    for user in users:
        birthdays_dict = dict()
        birthday_dt = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(datetime.today().date().year, birthday_dt.month, birthday_dt.day).date()

        if birthday_this_year.weekday() == 5:
            birthday_this_year +=timedelta(days = 2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year +=timedelta(days = 1)

        if birthday_this_year.year < next_seven_days.year:
            birthday_this_year = birthday_this_year.replace(year = birthday_this_year.year + 1)

        if next_seven_days > birthday_this_year >= date_today:
            birthdays_dict["name"] = user["name"]
            birthdays_dict["congratulation_date"] = datetime.strftime(birthday_this_year, "%Y.%m.%d")
            birthdays_lst.append(birthdays_dict)

    return birthdays_lst


if __name__ == "__main__":

    users = [
        {"name": "John Doe", "birthday": "1985.06.14"},
        {"name": "Jane Smith", "birthday": "1990.07.06"},
        {"name": "Jack Sparrow", "birthday": "1990.07.08"},
        {"name": "Taras Shevchenko", "birthday": "1985.08.22"},
    ]

    print(get_upcoming_birthdays(users))
