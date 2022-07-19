# Using break/continue on a nested loops of days and weeks (which you
# take as user input), encounter the scenario where we miss the first 2
# classes ever and still complete the syllabus one week before the end

weeks=int(input("Enter the week number:"))

for week in range(1,weeks+1):
    for day in range(1,6):
        if day<3 and week==1:
            continue
        print("week-",week,"Day_",day)
    if(week==weeks-1):
        break