from program import db

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default="My Todo list")
    
    items = db.relationship('TodoItem', backref='list', lazy='dynamic')

#includes all diferent item in the list. There will be relationship between TodoItem and TodoList
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listid = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    description = db.Column(db.String(100), nullable=False, default="")

    

