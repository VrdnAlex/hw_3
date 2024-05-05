from datetime import datetime


def get_days_from_today(date):
    try:
        date_input = datetime.strptime(date, "%Y-%m-%d").date()
        now_date = datetime.today
        diffence_day = now_date - date_input
        return diffence_day.days
    except ValueError:
        return ("Invalid date format")


print(get_days_from_today(date))
