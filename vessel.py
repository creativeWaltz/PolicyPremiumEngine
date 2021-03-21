import datetime


class Vessel:
    """Creates a vessel"""
    def __init__(self, name, imo, value):
        self.name = name
        self.imo = imo
        self.value = value
        self.value_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.owned = True
        self.sold_date = ""
        self.version = 1
        self.created_at_utc = datetime.datetime.utcnow().strftime("%d/%m/%Y")

    def sell(self, sale_date):
        """Sell the vessel and the date its sold"""
        if self.owned is False:
            print("This asset has already been sold")
        self.owned = False
        self.sold_date = sale_date

    def update_value(self, amount, new_value_date):
        """Update the value of the vessel and the date it changes"""
        if self.owned is False:
            print("You no longer own this vessel")
        elif "/" not in new_value_date:
            print("Incorrect date format")
        elif new_value_date <= self.value_date:
            print("New valuation date must be after current valuation date")
        elif amount == self.value:
            print("Value has not changed")
        else:
            self.value_date = new_value_date
            self.version += 1
            self.value = amount
