runTime = int(input("Enter the time taken to run in minutes (rounded): "))
swimTime = int(input("Enter the time taken to swim in mitutes (rounded): "))
cycleTime = int(input("Enter the time taken to cycle in mitutes (rounded): "))

def add(a,b,c):
    return a+b+c

totalTime = add(runTime,cycleTime,swimTime)
strTotalTime = str(totalTime)
print(str("your total time is " + strTotalTime + " you have been awarded:"))

if totalTime > 110:
    print("no award")

elif totalTime > 105:
    print("provincial scroll")

elif totalTime > 100:
    print("provincial half colours")

else:
    print("provincial colours")
