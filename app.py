from flask import Flask, Response, redirect
import logging, json, os

app = Flask(__name__)

#Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

#Files
SHORTENED_URLS_PATH = os.path.join(os.getcwd(), "shortened_urls.json")
@app.route("/")
def index():
    '''Returns a simple index.'''
    logger.info("Got a request to the index page.")
    return """Woof Woof! I'm a URL shortener. 
    Find me on GitHub: https://github.com/sotpotatis/simple_url_shortener
    """

@app.route("/<string:url_id>")
def shortened_url(url_id):
    '''Redirects to a shortened URL if found.
    If not, returns 404.'''
    logger.info("Got a request to the shortened URL endpoint.")
    #Load JSON with shortened URLs
    shortened_urls = json.loads(open(SHORTENED_URLS_PATH, "r").read())
    if url_id in shortened_urls:
        logger.info("URL was found, redirecting to it...")
        return redirect(shortened_urls[url_id])
    else:
        logger.info("URL was not found, returning 404...")
        return Response(status=404)