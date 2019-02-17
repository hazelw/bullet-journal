from bullet_journal import db

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80))

    def __repr__(self):
        return '<Collection %s: %s>' % (str(self.id), self.name)
