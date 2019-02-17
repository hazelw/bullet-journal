from app import app
from db import db


with app.app_context():
    db.create_all()

app.run(debug=True, host='0.0.0.0', port=5000)
