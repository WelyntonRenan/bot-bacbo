from flask import Flask
from config import Config
from routes.bot_routes import bot_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(bot_routes)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5002)