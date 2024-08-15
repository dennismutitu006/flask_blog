from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#from config import Config
from posts.blueprint import posts

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

app.register_blueprint(posts, url_prefix='/blog')


db = SQLAlchemy(app)
