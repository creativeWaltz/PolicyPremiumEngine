import datetime


class Vessel:
    """Creates a vessel"""
    def __init__(self, name, imo, value):
        self.name = name
        self.imo = imo
        self.value = value
        self.value_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.owned = True
        self.version = 1
        self.created_at_utc = datetime.datetime.utcnow()

    def sell(self):
        self.owned = False

    def update_value(self, amount, new_value_date):
        if "/" not in new_value_date:
            print("Incorrect date format")
        elif new_value_date <= self.value_date:
            print("New valuation date must be after current valuation date")
        elif amount == self.value:
            print("Value has not changed")
        else:
            self.value_date = new_value_date
            self.version += 1
            self.value = amount

