

import os

from flask import Flask
from api import bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

app = create_app()
app.register_blueprint(bp)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=5000)

