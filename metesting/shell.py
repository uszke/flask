from database import db
from database import User
db.create_all()
admin = User(username='krisi', email='krisi@example.com')
guest = User(username='pisi', email='pisi@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
User.query.all()
User.query.filter_by(username='hola').first()