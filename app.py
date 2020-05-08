from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    headers = {
        'authority': 'www.bukalapak.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': '__cfduid=dc70c67c9b8c1902fd2bd9b6044a88bd81586493811; identity=b453ff667fe4fdcc14b48398adca50aa; browser_id=1079b057b1ef1fb2e6db02942b18cf38; session_id=a107508f14913d066ba329cfc39a471e; osearch=Y2FsY3VsYXRvcjo1MTA6Y2FsY3VsYXRvcjpjYWxjdWxhdG9yOiQ5N2YxNGYzMS05YmNmLWFjZWQtOWY5My1hYzg3NGJkYmIyNTI7expires=0; keyword_parent_id=; keyword_correlation_id=opfgdq78c; __cfruid=6d8ad4c37d6980d44baa5f8125f7320c720db1f3-1588930173; __auc=799584eb171f39e674d2630469e; lskjfewjrh34ghj23brjh234=VWNoQWErU1ZsbngxZEl5dHNuSVFCZjJPK0lxNWptdzEvbVg2dFI4dGJBSmxUSlJrV0JKMDVMY2lURG5lbTB1TytUT3Z3V3J4L29HalRoaHNJNzBJcEhNbFRwMEhxZVJpVm9nRnR2UnlXektpZVV0WjZRQTFERG8zeTBlcDhVeDJmd2dnOEN6N2J0WmtnMWJoaEFMazVGL0pWWi9UcFE0d3ROK0haK1lUeVhCQnd4Y01EOG1mNVJ0dmwxMy9PYmtmSGZlMVdrUXIwc0M5R3R0T2s5bTJPOGlReW9BV1FyN3FjVkV5RkNlYnJQST0tLUdCQmcwR2ZISXhoMXpUVWxjQUZMM1E9PQ%3D%3D--79849156cf0e8fbc272d80f0c915c898dd7b29d3',
        'if-none-match': 'W/"ea8485d2715181cc30c5cf601b403cb6"',
    }

    params = (
        ('utf8', '\u2713'),
        ('source', 'navbar'),
        ('from', 'omnisearch'),
        ('search_source', 'omnisearch_organic'),
        ('from_keyword_history', 'false'),
        ('search[keywords]', 'calculator'),
    )

    response = requests.get('https://www.bukalapak.com/products', headers=headers, params=params)
    return response.content


if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run()
