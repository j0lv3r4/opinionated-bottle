from bottle import Bottle

app = Bottle()


@app.get("/")
def index():
    return "Hello, world"
