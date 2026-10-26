import re
import app as application


def test_index_shows_time():
    application.app.config["TESTING"] = True
    client = application.app.test_client()
    response = client.get("/")
    html = response.data.decode()
    # Verify a <p>Time: <code>...</code></p> block exists with an ISO 8601 timestamp
    match = re.search(r"<p>Time: <code>([^<]+)</code></p>", html)
    assert match, "Time line not found in response"
    # Basic ISO 8601 shape: YYYY-MM-DDTHH:MM:SS...+00:00
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", match.group(1))
