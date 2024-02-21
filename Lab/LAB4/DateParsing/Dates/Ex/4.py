import datetime, math

print("The shape of input: yyyy/mm/dd")
x = str(input("The first date: "))
y = str(input("The second date: "))

day1 = datetime.datetime.strptime(x, "%Y/%m/%d")
day2 = datetime.datetime.strptime(y, "%Y/%m/%d")
deltaday = (day2 - day1)
deltasec = (day2 - day1) * 86400

print ("The days differences:", abs(deltaday.days))
print ("The second differences:", abs(deltasec.days))