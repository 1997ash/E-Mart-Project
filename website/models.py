from website import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(10))
    brand = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String,nullable=False, default='default.jpg')
    link = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Product('{self.store},{self.description},{self.type},{self.brand},{self.price}')"