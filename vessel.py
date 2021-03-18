import datetime

class Vessel():
    "Creates a vessel"
    def __init__(self, name, imo):
        self.name = name
        self.imo = imo
        self.value = 0.0
        self.owned = True
        self.created_at_utc = datetime.datetime.utcnow()

    def sell(self):
        self.owned = False

    def update_name(self,name):
        self.name = name

    def update_imo(self,imo):
        self.imo = imo

    def update_value(self,value):
        self.value = value


