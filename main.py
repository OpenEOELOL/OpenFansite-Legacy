from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("<h1>Hello, world.</h1>")

if __name__ == "__main__":
    app.run()