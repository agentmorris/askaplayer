#!/usr/bin/python3
import flask
import sys
import logging
logging.basicConfig(stream=sys.stderr)
log = logging.getLogger(__name__)
log.error('Initializing WSGI')
sys.path.insert(0,"/var/www/html/dmorris/askaplayer/app")

from askacoach import create_app
application = create_app()

