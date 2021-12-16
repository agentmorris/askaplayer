#%% Constants and imports

import os
from flask import Flask
from flask import jsonify
from flask import render_template

from . import db


#%% App initialization

def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'askacoach.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'        
    
    @app.route('/')
    def home():
        return render_template('askacoach.html')

    @app.route('/request', methods=['POST','GET'])
    def request():
        dbobj = db.get_db()
        cursor = dbobj.execute("SELECT * FROM responses ORDER BY RANDOM() LIMIT 1;")
        s = cursor.fetchone()['response']
        print('Retrieved {}'.format(s))
        return jsonify(response=s)
        
    db.init_app(app)
    
    return app

