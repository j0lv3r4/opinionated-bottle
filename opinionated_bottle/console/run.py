import click
from bottle import run

from opinionated_bottle.server.server import app
from opinionated_bottle.settings import HOST, PORT, DEBUG, RELOADER


@click.command()
def cli():
    """Start bottle server"""

    run(app=app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)
