# cafe menu list 

menu = [ 'coffee','tea','Cake','Sandwich']
# stock dictionary
stock = {
 'coffee' : 100,
 'tea' :  50,
 'Cake' : 20,
 'Sandwich' : 30
}

# price dictionary 
price = {
'coffee' : 2.50,
'tea' : 1.50,
'Cake' : 3,
'Sandwich' : 5
}
# Calculation 
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value
# print the result 
print(f'The total stock in the cafe is; £{total_stock_worth: .2f}')