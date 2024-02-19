
class InvestorModule:
    def input_invest(self):
        self.invest_input = float(input("Enter your Investment Details in Rs : "))
        self.investment_duration = int(input("Enter investment duration in months: "))

    def profit_loss(self, cost_price, selling_price):
        profit = selling_price - cost_price
        loss = cost_price - selling_price
        if profit > loss:
            return True, profit
        else:
            return False, loss

    def display_investment_details(self, cost_price, selling_price, profit, loss):
        print("Your total investment is :", self.invest_input)
        print("Your investment duration is :", self.investment_duration, "months")
        print("Your projection profit amount is :", profit)
        print("Your projection loss amount is :", loss)


class Investor(InvestorModule):
    def __init__(self):
        super().__init__()
    def input_invest(self):
        super().input_invest()

    def profit_loss(self, cost_price, selling_price):
        return super().profit_loss(cost_price, selling_price)

    def display_investment_details(self, cost_price, selling_price, profit, loss):
        super().display_investment_details(cost_price, selling_price, profit, loss)


invest = Investor()
invest.input_invest()

cost_price = float(input("Enter the cost price : "))
selling_price = float(input("Enter the Selling price : "))

if invest.profit_loss(cost_price, selling_price)[0]:
    print("The projection amount will be : ")
    profit = invest.profit_loss(cost_price, selling_price)[1]
    Percentage = (profit / cost_price) * 100
    if profit > cost_price:
        print("Profit",profit)
        print("Percentage",Percentage)
    loss = 0
else:
    print("For the investment amount, the projection price will be : ")
    loss = invest.profit_loss(cost_price, selling_price)[1]
    profit = 0

invest.display_investment_details(cost_price, selling_price, profit, loss)

