from db import db


class WeedProductModel(db.Model):
    __tablename__ = 'weedproduct'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    crop = db.Column(db.String(80))
    product = db.Column(db.String(80))
    dose = db.Column(db.String(80))
    country = db.Column(db.String(80))
    # ------19-10-20----------------------------------------------------
# ------19-10-20-----Country----------------------------------------
    def __init__(self, name, crop, product, dose, country):
        self.name = name
        self.crop = crop
        self.product = product
        self.dose = dose
        self.country = country
# ------19-10-20----------------------------------------------------

# ------19-10-20-----Country Crop----------------------------------------

    def json(self):
        return {'name': self.name, 'product': self.product, 'dose': self.dose, 'crop': self.crop, 'country': self.country}

# ------19-10-20----------------------------------------------------------

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)

# -------19-10-20-------Find Item Object before populating----------------------------------------
    @classmethod
    def find_object(cls, item_obj):
        # print(item_obj)
        item = cls.query.filter_by(name=item_obj.name, product=item_obj.product, crop=item_obj.crop, dose=item_obj.dose, country=item_obj.country).scalar()
        # print(item)
        if item:
            return True
        else:
            return False
# -------19-10-20---------------------------------------------------------------------------------

# -------19-10-20--------Find Product---------------------------------------------

    @classmethod
    def find_product(cls, name, crop, country):
        # print(item_obj)
        item = cls.query.filter_by(name=name, crop=crop,country=country)
        return item
        # print(item)
        # if item:
        #     return True
        # else:
        #     return False

# -------19-10-20-----------------------------------------------------------------

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
