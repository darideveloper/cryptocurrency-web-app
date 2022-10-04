from flask import Flask
from routes.api import blueprint_api
from routes.home import blueprint_home

application = Flask (__name__)

# Register blueprints
application.register_blueprint (blueprint_home, url_prefix="/")
application.register_blueprint (blueprint_api, url_prefix="/api")

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()