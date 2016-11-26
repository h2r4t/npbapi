import calendar

def cal():
    c = calendar.TextCalendar(calendar.SUNDAY)
    test = c.formatmonth(2016,9)
    return test
