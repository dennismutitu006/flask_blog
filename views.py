# to handle user requests
from app import app

@app.route('/')
def index():
  return 'Hello world'
