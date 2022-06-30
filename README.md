# Simple URL Shortener

I needed a *simple* URL shortener. Emphasis on simple.
I keep the project on GitHub mainly because I needed to transfer
the code between devices myself.

### Setup
* `pip install -r requirements.txt`
* Edit `shortened_urls.json` to your liking, see the example. (mapping is `URL ID` --> `URL`)
* Run the server, for example with `gunicorn app:app`.