destinations = """
List of holiday destinations:
Paris £15
Berlin £20 
Warsaw £25
Rome £30
"""      #lists the hoiday options with flight prices

print(destinations) 
city_flight = input("Please choose a holiday destination from the list above: ")
num_nights = int(input("How many nights will you be staying? 1 night is £60: "))
rental_days = int(input("How many days will you want a rental car for? 1 day is £30: "))

#asks the user for their holiday information

# if city_flight != "paris" or "berlin" or "Warsaw" or "Rome":
#     break
# else print(" ")

def hotel_cost(x):
    y = x * 60
    return y

print("Your Hotel will cost will be: £" + str(hotel_cost(num_nights)) + " for " + str(num_nights) + " days.")

#Tells the user the hotel costs

def plane_cost(x):
    if city_flight == "Paris":
        x = (15)
    elif city_flight == "Berlin":
        x = (20)
    elif city_flight == "Warsaw":
        x = (25)
    elif city_flight == "Rome":
        x = (30)
    else:
        x = "Try again"
    return x

print("Your flights will cost £" + str(plane_cost(city_flight)) + " in total.")
    
#tells the user their flight cost

def car_rental(x):
     y = x * 30
     return y

print("Your car rental will cost £" + str(car_rental(rental_days)) + " for " + str(rental_days) + " days.") 

#tells the user their car rental cost

def holiday_cost(a,b,c):
    w = hotel_cost(a) + plane_cost(b) + car_rental(c)
    return w

print("The total for your holiday will be £" + str(holiday_cost(num_nights, city_flight, rental_days)) + ".")
#tells the user their total holiday cost