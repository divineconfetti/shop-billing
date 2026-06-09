#shopping cart
import pandas as pd

items = []
prices = []
sell_price = []

while True:
  item = input("Enter your items here: ")
  if item.lower() == 'q':
    break
  # elif item == q:
  #   print('Invalid Response')
  else:
    mrp_cost = int(input("The total cost of this item is: "))
    prices.append(mrp_cost)
    discount_price = int(input("The discounted price of item is: "))
    sell_price.append(discount_price)
    items.append(item)
total_cost = sum(prices)
total_discount = sum(sell_price)
bill = {'Item': items, 'Cost': prices, 'Discount': sell_price}
df1= pd.DataFrame(bill)
totals_row = {'Item': 'Total', 'Cost': total_cost, 'Discount': total_discount}
df2= pd.DataFrame([totals_row])
df = pd.concat([df1, df2], ignore_index=True)
print()
print("--- Here's the total bill---")
print()
print(df)
edit = input("Would you like to edit the items? To edit the list press E, if no press N")
if edit.lower() == 'e':
  a= input("Enter the index of the item you want to remove: ")
  df = df.drop(index=int(a)).reset_index(drop=True)
elif edit.lower() == 'n':
  print()
print("--- Here's the total bill---")
print()
print(df)