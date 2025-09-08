# Data Types in Python
from pyscript import display


restaurant_name = 'BAMYUM' # String
owner_name = 'Tessa Aseo' # String
year_established = 2001 # Integer
popular_item_price = 1331 # Integer
has_delivery = True # Boolean
product_names = ['Gilded Hall', 'Almond Tofu', 'Jade Parcels','Cassoulet', 'Crystal Shrimp'] # List
business_hours = '9:00 AM to 10:00 PM Daily' # String

menu_prices = [
    '1331' , '1200' , '750' , '250' , '130' 
 ] # List

common_allergens = ['soybeans', ] # List
tax_rate = 0.2 #Float

display(f'{restaurant_name}', target='Restaurant')
display(f'Owned by {owner_name}', target='Owner')
display(f'Since {year_established}', target='since')
display(f'Open hours: {business_hours}.', target='opening')

#
display(f'{menu_prices[0]}', target='price1')
display(f'{menu_prices[1]}', target='price2')
display(f'{menu_prices[2]}', target='price3')
display(f'{menu_prices[3]}', target='price4')
display(f'{menu_prices[4]}', target='price5')

display(f'{product_names[0]} ★', target='product1')
display(f'{product_names[1]} ★', target='product2')
display(f'{product_names[2]}', target='product3')
display(f'{product_names[3]}', target='product4')
display(f'{product_names[4]}', target='product5')



