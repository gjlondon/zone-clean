import calendar
import pprint
import random
import collections
import datetime

d = collections.deque(["Roomie", "Other Roomie", "It's Me!"])
zones = ["Kitchen", "Bathroom", "Everything Else"]
random.shuffle(d)
this_month = int(datetime.datetime.now().month)

for month in range(this_month,
                   this_month + 12):
    if month > 12:
        month -= 12
    c = calendar.monthcalendar(2013, month)
    for week in c:
        sun = week[-1]
        if sun == 0:
            continue
        print "\nWeek ending {}-{}\n".format(month, sun)
        for line in zip(zones, d):
            print "{}:\t{}".format(*line)
        d.rotate(1)
        

