class InvestorModule:
    def input_invest(self):
        print("#####################################################################################")
        self.initial_investment = 30000000  # Initial investment in manufacturing unit
        self.productivity = 50000  # Per month
        self.cost_of_production = float(input("Enter total expenses including raw materials, salaries, and consumables per month: "))
        self.cost_of_one_brick = float(input("Enter the cost of one brick: "))
        self.selling_price = self.cost_of_one_brick * self.productivity
        self.depreciation = (5/100 * 30000000) / 12
        self.invest_input = float(input("Enter your investment details in Rs: "))
        print("#####################################################################################")
    def profit_loss(self):
        profit = self.selling_price - self.cost_of_production - self.depreciation
        loss = self.cost_of_production - self.selling_price - self.depreciation
        return profit, loss

    def display_investment_details(self, profit, loss):
        print("#####################################################################################")
        print("Your initial investment in the manufacturing unit: Rs.", self.initial_investment)
        print("Your monthly production:", self.productivity, "bricks")
        print("Your monthly cost of production: Rs.", self.cost_of_production)
        print("Your selling price per brick: Rs.", self.cost_of_one_brick)
        print("Your monthly selling price: Rs.", self.selling_price)
        print("Your monthly depreciation cost: Rs.", self.depreciation)
        print("Your total investment: Rs.", self.invest_input)
        print("#####################################################################################")
        if profit > loss:
            print("Your projected profit amount: Rs.", profit)
        else:
            print("Your projected loss amount: Rs.", loss)


class Investor(InvestorModule):
    def __init__(self):
        super().__init__()

    def input_invest(self):
        super().input_invest()

    def profit_loss(self):
        return super().profit_loss()

    def display_investment_details(self, profit, loss):
        super().display_investment_details(profit, loss)


invest = Investor()
invest.input_invest()

profit, loss = invest.profit_loss()

if profit > loss:
    print("Congratulations! You're making a profit.")
else:
    print("You're experiencing a loss.")

invest.display_investment_details(profit, loss)