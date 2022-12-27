from market import db, app, Item

with app.app_context():
    print(Item.query.all())
