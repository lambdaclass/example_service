import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    branch = os.environ.get("PREVIEW_BRANCH", "unknown")
    host = os.environ.get("PREVIEW_HOST", "localhost")
    return (
        "<html><body>"
        "<h1 style=\"color: red;\">CHAU</h1>"
        "<img src=\"https://graffitimundo.com/wp-content/uploads/2011/01/nestor-x-41-773x480.jpg\""
        " alt=\"Nestornauta\" style=\"max-width: 400px; display: block; margin: 20px auto;\">"
        "<p style=\"text-align: center; font-size: 1.2em; font-weight: bold;\">"
        "Soberan&iacute;a tecnol&oacute;gica y nacional: el futuro se construye con memoria, verdad y justicia.</p>"
        f"<p>Branch: <code>{branch}</code></p>"
        f"<p>Host: <code>{host}</code></p>"
        "</body></html>"
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
