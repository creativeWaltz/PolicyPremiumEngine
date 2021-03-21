import datetime


class Vessel:
    """Creates a vessel"""
    def __init__(self, name, imo, value):
        self.name = name
        self.imo = imo
        self.value = value
        self.value_date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.owned = True
        self.version = 1
        self.created_at_utc = datetime.datetime.utcnow()

    def sell(self):
        self.owned = False

    def update_value(self, value, amount, new_value_date):
        if new_value_date <= str(self.value_date):
            print("Must be after current date")
        else:
            self.value_date = new_value_date
            self.version += 1
            self.value = amount

