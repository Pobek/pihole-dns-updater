from flask import Flask

from config import Config
from app import util

app = Flask("pihole-proxy")
cfg = Config()

from app import routes