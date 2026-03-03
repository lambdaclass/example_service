import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    branch = os.environ.get("PREVIEW_BRANCH", "unknown")
    host = os.environ.get("PREVIEW_HOST", "localhost")
    return (
        "<html><body style='text-align: center; font-family: sans-serif;'>"
        "<h1 style='color: red;'>CHAU</h1>"
        "<img src='https://graffitimundo.com/wp-content/uploads/2011/01/nestor-x-41-773x480.jpg'"
        " alt='Nestornauta' style='max-width: 480px; width: 100%;'>"
        "<h2>Soberanía tecnológica y nacional</h2>"
        "<img src='https://i.imgflip.com/2/1h2u3g.jpg'"
        " alt='Pepe Hacker' style='max-width: 300px; width: 100%;'>"
        f"<p>Branch: <code>{branch}</code></p>"
        f"<p>Host: <code>{host}</code></p>"
        "</body></html>"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
