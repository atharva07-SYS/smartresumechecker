

import os
import nltk
from flask import Flask

# Set NLTK data path to project-local nltk_data directory
NLTK_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'nltk_data'))
if NLTK_DATA_PATH not in nltk.data.path:
    nltk.data.path.insert(0, NLTK_DATA_PATH)
print('CWD:', os.getcwd())
print('NLTK_DATA_PATH:', NLTK_DATA_PATH)
print('NLTK_DATA_PATH exists:', os.path.exists(NLTK_DATA_PATH))
print('NLTK data path list:', nltk.data.path)

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
