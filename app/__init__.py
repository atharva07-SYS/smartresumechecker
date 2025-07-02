
from flask import Flask
import os
import nltk
nltk.data.path.append('/opt/render/nltk_data')
nltk.download('punkt', download_dir='/opt/render/nltk_data')
nltk.download('stopwords', download_dir='/opt/render/nltk_data')

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
