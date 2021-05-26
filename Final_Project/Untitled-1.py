
class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    counry_name=db.Column(db.String(50))
    country_states=db.relationship('State',backref='country')

class State(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    state_name=db.Column(db.String(50))
    country_id=db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)
