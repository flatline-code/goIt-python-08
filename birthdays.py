# Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо 
# поздравить с днём рождения на неделе.

# У вас есть список словарей users, каждый словарь в нём обязательно имеет 
# ключи name и birthday. Такая структура представляет модель списка 
# пользователей с их именами и днями рождения. name — это строка с именем 
# пользователя, а birthday — это datetime объект, в котором записан день 
# рождения.

# Ваша задача написать функцию get_birthdays_per_week, которая получает на вход 
# список users и выводит в консоль (при помощи print) список пользователей, 
# которых надо поздравить по дням.

# Условия приёмки
# get_birthdays_per_week выводит именинников в формате:
# Monday: Bill, Jill
# Friday: Kim, Jan

# Пользователей, у которых день рождения был на выходных, надо поздравить в 
# понедельник. Для отладки удобно создать тестовый список users и заполнить 
# его самостоятельно. Функция выводит пользователей с днями рождения на неделю 
# вперед от текущего дня. Неделя начинается с понедельника.

from datetime import datetime, timedelta

alex_birthday = datetime(year=1989, month=11, day=9)

users = [{'name': 'Alex', 'birthday': datetime(year=1989, month=9, day=23)},
         {'name': 'Bob', 'birthday': datetime(year=1983, month=9, day=23)},
         {'name': 'Rick', 'birthday': datetime(year=2012, month=9, day=23)}]

def get_birthdays_per_week(users):
    result_obj = {0: ['Monday', []], 1: ['Tuesday', []], 2: ['Wednesday', []],
                  3: ['Thursday', []], 4: ['Friday', []], 5: ['Monday', []], 
                  6: ['Monday', []]}

    today = datetime.now().date()
    delta = timedelta(days=7)

    for user in users:
        birthday = user['birthday']
        user_next_birthday = datetime(year=today.year, 
                                      month=birthday.month, 
                                      day=birthday.day).date()

        if user_next_birthday < today:
            continue
        if user_next_birthday - today > delta:
            continue
        
        weekday = user_next_birthday.weekday()
        result_obj[weekday][1].append(user['name'])

    for names in result_obj.values():
        if names[1]:
            print(f"{names[0]}: {', '.join(names[1])}")

get_birthdays_per_week(users)