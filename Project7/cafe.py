'''This program lists a menu as a variable, lists the stock and prices for each item in a list,
it returns the total stock price for each product and a overall stock value. '''

menu = ["BLT", "Chips", "Fish", "Watermelon"]     #menu 

stock = {"BLT": 12,                                  #list of the items and their stock number
         "Chips": 20,
         "Fish": 8,
         "Watermelon": 4}

price = {"BLT": 3,                                  #list of the items and their price
         "Chips": 1.2,
         "Fish": 3.8,
         "Watermelon": 2.4}

total_stock = {key: price.get(key) * stock.get(key)    #saves the key side(products) and multiplys the stock num by the price per
for key in stock.keys()}                               #for each key in stock keys

print("The total value of each products stock is (£): " + str(total_stock))

total_cost = sum(total_stock.values())                   #adds all the totals together for the overall price
print("The total value of the stock is £" + str(total_cost))