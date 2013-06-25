import calendar
import pprint
import random
import collections

peps = ["Roomie", "Other Roomie", "It's Me!"]
random.shuffle(peps)
d = collections.deque(peps)

for month in range(6, 13):

    c = calendar.monthcalendar(2013, month)
    for week in c:
        sun = week[-1]
        if sun == 0:
            continue
        print "{}-{}".format(month, sun)
        print """
        Kitchen: {}
        Bathroom: {}
        Living Room / Trash: {}
        """.format(d[0], d[1], d[2])
        d.rotate(1)
        

