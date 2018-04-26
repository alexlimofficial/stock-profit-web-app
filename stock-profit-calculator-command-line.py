"""
Python Stock Profit Calculator - CLI Version

Author: Alex Lim
"""

# Get all input information from user
print('Compute your profit')
ticker_symbol = input('Ticker Symbol? ')
allotment = float(input('Allotment (Number of shares)? '))
final_share_price = float(input('Final Share Price (in dollars)? '))
sell_commission = float(input('Sell Commission (in dollars)? '))
initial_share_price = float(input('Initial Share Price (in dollars)? '))
buy_commission = float(input('Buy Commission (in dollars)? '))
capital_gain_tax_rate = float(input('Capital Gain Tax Rate (in %)? '))

# Proceeds
proceeds = allotment * final_share_price
print('Proceeds:', '$' + str(proceeds))

# Cost
initial_purchase_cost = allotment * initial_share_price
profits = proceeds - initial_purchase_cost - buy_commission - sell_commission
capital_tax = capital_gain_tax_rate / 100.00
tax_on_capital_gain = profits * capital_tax
cost = initial_purchase_cost + sell_commission + buy_commission + \
       tax_on_capital_gain
print('Cost:', '$' + str(cost))

# Cost Details
print('Total Purchase Price')
print(allotment, 'X', initial_share_price, '=', initial_purchase_cost)
print('Buy Commission =', buy_commission)
print('Sell Commission =', sell_commission)
print('Tax on Capital Gain =', str(capital_gain_tax_rate) + '%', 'of', '$'
      + str(profits), '=', '$' + str(tax_on_capital_gain))

# Net Profit
net_profit = proceeds - cost
print('Net Profit')
print('$' + str(net_profit))

# Return on Investment
return_on_investment = (net_profit / cost) * 100
print('Return on Investment')
print('{0:.2f}%'.format(return_on_investment))

# Break even
cost_per_share_after_commission = initial_purchase_cost + buy_commission + \
                                  sell_commission
break_even_price = cost_per_share_after_commission / allotment
print('To break even, you should have a final share price of')
print(break_even_price)
