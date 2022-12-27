from market.models import db
from market import app
with app.app_context():
    db.create_all()
    #print(Item.query.all())