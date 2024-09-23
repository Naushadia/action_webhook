from flask import Flask

from app.webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        return "Welcome to our homepage!"

    # registering all the blueprints
    app.register_blueprint(webhook)

    return app
