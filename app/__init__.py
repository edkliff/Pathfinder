from configs.backend_settings import START_POINT, FINISH_POINT
from flask import Flask

app = Flask(__name__)
from app import api

app.run(debug=True)