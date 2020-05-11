# python 3

# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.

# Examples
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796

# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }) ➞ 32411

# profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }) ➞ 44030


def profit(info):
	return round((info.get('sell_price')-info.get('cost_price'))*info.get('inventory'))



if __name__ =='__main__':

	print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))




	print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))