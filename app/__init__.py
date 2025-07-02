

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
import glob
print('nltk_data contents:', os.listdir(NLTK_DATA_PATH))
punkt_dir = os.path.join(NLTK_DATA_PATH, 'tokenizers', 'punkt')
if os.path.exists(punkt_dir):
    print('punkt contents:', os.listdir(punkt_dir))
else:
    print('punkt directory does not exist!')
print('All punkt files:', glob.glob(os.path.join(NLTK_DATA_PATH, 'tokenizers', 'punkt', '*')))
print('All punkt PY3 files:', glob.glob(os.path.join(NLTK_DATA_PATH, 'tokenizers', 'punkt', 'PY3', '*')))

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
