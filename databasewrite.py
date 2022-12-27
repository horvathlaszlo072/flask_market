from market import db, app
from market.models import Item, User

with app.app_context():
    #u1 = User(username='jsc', password_hash='123456', email_address='jsc@jsc.com')
    #item2 = Item(name="Laptop", price=600, barcode='321912987542', description='description')
    #i1 = Item(name="IPhone 10", price=800, barcode='123456789012', description='megjegyzés')
    #db.session.add(i1)
    #db.session.commit()
    #print(Item.query.all())
    item1 = Item.query.filter_by(name='IPhone 10').first()
    item1.owner = User.query.filter_by(username='jsc').first().id
    db.session.add(item1)
    db.session.commit()
    print(item1.owner)