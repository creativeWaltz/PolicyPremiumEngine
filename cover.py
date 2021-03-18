class CoverType():
    "Creates a cover type for a policy"
    def __init__(self, name,rate):
        self.name = name
        self.rate = rate
        self.deductiom = 0.00

    #Update the rate
    def change_rate(self, rate):
        self.rate = rate

    #Update the deduction
    def change_deduction(self, deduction):
        self.deductiom = deduction
