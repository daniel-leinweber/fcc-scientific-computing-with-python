from datetime import datetime, timedelta
from dateutil.parser import parse

def add_time(start, duration, day=None):
  
  hours_to_add, minutes_to_add = map(int, duration.split(':'))
  start_date_time = parse(start)

  if day != None:
    weekday = datetime.strftime(start_date_time, '%A').lower()
    while weekday != day.lower():
      start_date_time += timedelta(days = 1)
      weekday = datetime.strftime(start_date_time, '%A').lower()

  final_date_time = start_date_time + timedelta(hours = hours_to_add, minutes = minutes_to_add)

  time_format = '%-I:%M %p'
  final_time = datetime.strftime(final_date_time, time_format)

  day_difference = (final_date_time.date() - start_date_time.date()).days

  if day != None:
    new_week_day = datetime.strftime(final_date_time, '%A')
    final_time = f'{final_time}, {new_week_day}'

  if day_difference > 1:
    return f'{final_time} ({day_difference} days later)'
  elif day_difference > 0:
    return f'{final_time} (next day)'
  else:
    return final_time