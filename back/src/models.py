from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Tarea(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key=True)
    tarea = db.Column(db.String(200))

    def serialize(self):
        return{
            "id": self.id,
            "tarea": self.tarea
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit(self)