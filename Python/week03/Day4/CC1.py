# Using break/continue on a nested loops of days and weeks (which you
# take as user input), skip out on the even days of all odd weeks.

week=int(input("Enter week number:"))
for week in range(1,week+1):
    for day in range(1,6):
        if day%2==0 and week %2==1:
            continue
        print("week-",week, "Day-",day)