from flask import Flask


def create_app():
    app = Flask(__name__)

    register_blueprints(app)
    return app


def register_blueprints(app):
    from auth.views import bp as auth
    app.register_blueprint(auth)

    from example.views import bp as example
    app.register_blueprint(example)
