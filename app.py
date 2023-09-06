from flask import Flask
from controllers.crt_todo import bp as bp_crt_todo


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="static",
        instance_relative_config=True,
    )

    app.config.from_mapping(
        SECRET_KEY="super secret key",
        SESSION_TYPE="filesystem",
        JSONIFY_PRETTYPRINT_REGULAR=False,
    )

    app.register_blueprint(bp_crt_todo)
    return app
