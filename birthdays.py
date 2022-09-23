from datetime import datetime, timedelta

users = [{'name': 'Alex', 'birthday': datetime(year=1989, month=9, day=24)},
         {'name': 'Bob', 'birthday': datetime(year=1983, month=9, day=28)},
         {'name': 'Rick', 'birthday': datetime(year=2012, month=10, day=1)}]

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