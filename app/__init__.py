
from flask import Flask
from config import Config
from model import Model
from beam import BeamSearch

app = Flask(__name__)
app.config.from_object(Config)

#from app import routes
import routes

if __name__ == '__main__':
    print("RUN IT")
    app.run(threaded=True)
