import datetime

class Policy():
    "Creates a policy"
    def __init__(self, name,start_date, end_date):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date,"%d/%m/%Y")
        self.end_date = datetime.datetime.strptime(end_date,"%d/%m/%Y")
        self.currency = "usd"
        self.created_at_utc = datetime.datetime.utcnow()
        self.duration = self.end_date - self.start_date
        self.assets = []
        self.premiums = []
        self.covers = []

    def total_assets(self):
        count_assets = 0
        for asset in self.assets:
            count_assets +=1
        return count_assets

    def sum_premium(self):
        sum_premium = 0

    def update_name(self,name):
        self.name = name

    def add_assets(self,vessel):
        self.assets.extend(vessel)

    def add_covers(self,covers):
        self.covers.extend(covers)

    def display_details(self):
        print("Policy name: ", self.name)
        print("Start: ", self.start_date)
        print("End: ", self.end_date)
        print("Currency: ", self.currency.upper())
        print("Created: ", self.created_at_utc)
        print("Duration: ", self.duration)
        print("Total Assets:",self.total_assets())
        print("Assets: ")
        for asset in self.assets:
            print(f"\t{asset.name}")
        print("Covers:")
        for cover in self.covers:
            print(f"\t{cover.name} {cover.rate}% ")
        print("Premiums: ", self.premiums)
