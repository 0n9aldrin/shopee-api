from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = "https://www.bukalapak.com/products?utf8=✓&source=navbar&from=omnisearch&search_source=omnisearch_organic&from_keyword_history=false&search%5Bkeywords%5D=calculator"
    r = requests.get(url)
    return r.content


if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run()
