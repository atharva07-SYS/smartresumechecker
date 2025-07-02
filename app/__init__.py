
from flask import Flask
import os
import nltk
nltk_data_dir = '/tmp/nltk_data'
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.clear()
nltk.data.path.append(nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir, force=True)
nltk.download('stopwords', download_dir=nltk_data_dir, force=True)

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
