class Mydata(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    number = db.Column(db.Numeric(20,6))
    messtype = db.Column(db.String(30))
    anothernumber = db.Column(db.Numeric(20,2))
    ts = db.Column(db.TIMESTAMP)
    def __init__(self, number, gpsy, messtype, anothernumber, ts):
        self.number = number
        self.messtype = messtype
        self.anothernumber = anothernumber
        self.ts = ts

def __repr__(self):
    return self.messtype