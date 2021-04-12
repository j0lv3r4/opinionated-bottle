from opinionated_bottle.server.server import app


@app.get("/")
def index():
    return "Hello, world."
