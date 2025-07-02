
from flask import Flask
import os
import nltk

# Download required NLTK data if not already present
nltk.download('punkt')
nltk.download('stopwords')

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure uploads directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
