import datetime

class Policy():
    "Creates a policy"
    def __init__(self, name,start_date, end_date):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date,"%d/%m/%Y")
        self.end_date = datetime.datetime.strptime(end_date,"%d/%m/%Y")
        self.curreny = "usd"
        self.created_at_utc = datetime.datetime.utcnow()
        self.duration = self.end_date - self.start_date

    def sell(self):
        self.owned = False

    def update_name(self,name):
        self.name = name

    def update_imo(self,imo):
        self.imo = imo

    def update_value(self,value):
        self.value = value