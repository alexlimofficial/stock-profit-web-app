"""
Stock Profit Calculator Web Application

Author: Alex Lim
"""

# Import Flask packages
from flask import Flask, render_template, request

# Define an instance of Flask object
app = Flask(__name__)

# Defines the routes and view function
@app.route('/submit', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def calculator():
    # If a POST request is coming through to send route --> process information
    if request.method == 'POST':

        """ Retrieve inputs given to form and store in variables """

        ticker = request.form['ticker']

        allotment = float(request.form['allotment'])
        final_share_price = float(request.form['final_price'])
        sell_commission = float(request.form['sell_commission'])
        initial_share_price = float(request.form['initial_share_price'])
        buy_commission = float(request.form['buy_commission'])
        capital_gain_tax = float(request.form['capital_gain_tax'])

        """ Do calculations on inputs """

        # Proceeds
        proceeds = allotment * final_share_price

        # Cost
        initial_purchase_cost = allotment * initial_share_price
        profits = proceeds - initial_purchase_cost - buy_commission - sell_commission
        capital_tax = capital_gain_tax / 100.00
        tax_on_capital_gain = profits * capital_tax
        cost = initial_purchase_cost + sell_commission + buy_commission + tax_on_capital_gain

        # Net Profit
        net_profit = proceeds - cost

        # Return on Investment
        return_on_investment = round((net_profit / cost) * 100, 2)

        # Break Even Price
        cost_per_share_after_commission = initial_purchase_cost + buy_commission + sell_commission
        break_even_price = cost_per_share_after_commission / allotment

        """ Render HTML template (report.html) with passed arguments """

        return render_template('report.html', ticker=ticker, allotment=allotment, final_share_price=final_share_price,
                               sell_commission=sell_commission, initial_share_price=initial_share_price, cost=cost,
                               buy_commission=buy_commission, capital_gain_tax=capital_gain_tax, proceeds=proceeds,
                               initial_purchase_cost=initial_purchase_cost, profits=profits, net_profit=net_profit,
                               tax_on_capital_gain=tax_on_capital_gain, return_on_investment=return_on_investment,
                               break_even_price=break_even_price)

    # If not POST request, it is a GET request. Return render_template: 'calculator.html'
    return render_template('calculator.html')

if __name__ == "__main__":
    app.run()
