import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    branch = os.environ.get("PREVIEW_BRANCH", "unknown")
    host = os.environ.get("PREVIEW_HOST", "localhost")
    return (
        "<html><body>"
        "<h1>Hello, World!</h1>"
        f"<p>Branch: <code>{branch}</code></p>"
        f"<p>Host: <code>{host}</code></p>"
        "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"
        "</body></html>"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
