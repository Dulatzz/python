import datetime
o = datetime.timedelta(days = 1)
x = datetime.datetime.today() - o
y = datetime.datetime.today()
z = datetime.datetime.today() + o

print("Yesterday:", x.strftime("%A"))
print("Today:", y.strftime("%A"))
print("Tomorrow:", z.strftime("%A"))