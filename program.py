from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path="", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://jjehlik:tissuEa@DESKTOP-KS6CF9G/flask"
    #connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

    db.init_app(app)

    with app.app_context():
        from mainroutes import routes
        app.register_blueprint(routes)

        db.create_all()
        return app

    
