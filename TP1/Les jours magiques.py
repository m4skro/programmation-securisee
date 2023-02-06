#Exercice 5 Mascaro Matteo
#Les jours Magiques
import datetime

def is_magic_day(date):
    day_of_week = date.strftime("%A")
    day_number = date.strftime("%d")
    if (int(day_number) + len(day_of_week)) % 10 == 0:
        return True
    return False

def count_magic_days(start_date, end_date):
    magic_days = 0
    current_date = start_date
    while current_date <= end_date:
        if is_magic_day(current_date):
            magic_days += 1
        current_date += datetime.timedelta(days=1)
    return magic_days

start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime.now()
magic_days_count = count_magic_days(start_date, end_date)
print("Number of magic days between", start_date, "and", end_date, ":", magic_days_count)
