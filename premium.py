class Premium():
    "Creates a premium for a vessel for a cover type"
    def __init__(self):
        self.amount = 0
        self.currency = "usd"
        self.rate = 0

    #Calculate the inception premium on a vessel
    def calculate_inception_premium(self,vessel, cover, policy):
        self.amount = policy.duration * policy.rate * vessel.value
        return self.amount

