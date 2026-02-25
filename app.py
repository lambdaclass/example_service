import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    branch = os.environ.get("PREVIEW_BRANCH", "unknown")
    host = os.environ.get("PREVIEW_HOST", "localhost")
    return (
        "<html><body>"
        "<img src='https://lh3.googleusercontent.com/ci/AL18g_T_eAsriPtJJ6fj5JHS_RLRuUI-UWVa3WaAKEJZaSkseObb-wkbsHbe5f7b6LLXAj4I84Dw5OQ' alt='El Nestornauta' style='max-width:300px'/>"
        "<p><strong>Soberanía tecnológica y nacional</strong></p>"
        "<h1>Hello, World!</h1>"
        "<p>whats poppin</p>"
        f"<p>Branch: <code>{branch}</code></p>"
        f"<p>Host: <code>{host}</code></p>"
        "</body></html>"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
