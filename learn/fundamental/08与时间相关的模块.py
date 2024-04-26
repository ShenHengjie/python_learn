import time
import datetime
import calendar

t = time.localtime()
print('t-->', t)
print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.min)
print(datetime.date.max)

calendar.setfirstweekday(1)
print(calendar.firstweekday())
print(calendar.isleap(2019))
print(calendar.leapdays(1945, 2019))
print(calendar.weekday(2019, 12, 1))
print(calendar.monthrange(2019, 12))
print(calendar.month(2019, 12))
print(calendar.prcal(2019))