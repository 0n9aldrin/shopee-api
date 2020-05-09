from flask import Flask
import requests
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()

def getShopee(keyword):
        result_data_list = []
        headers = {
            'authority': 'shopee.co.id',
            'x-requested-with': 'XMLHttpRequest',
            'if-none-match-': '55b03-e17607803099ed81f4097a6d08057af3',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-api-source': 'pc',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://shopee.co.id/search?keyword=' + keyword,
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': '_gcl_au=1.1.462705111.1588794535; _fbp=fb.2.1588794535066.447793156; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=msmAArgoZQQynd8y4m8zFGqOAOrFv02z; REC_T_ID=9e6f0c7e-8fd2-11ea-a4b9-ccbbfe5de5ff; SPC_SI=98bhb0q6ym7fbej4utjk4euft93n43sf; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.623474330.1588794537; _gid=GA1.3.1283352780.1588794537; SPC_CT_c312ba2b="1588794565.Nlp8wfA3Ir+Zx2s5thu3KHxfkIzRQgpjCnfQ/GC1sJ4="; SPC_R_T_ID="h5sEB8bcl/05iuSfyphx4JGe1GU4SGMajYQKEeKMntGP8JaaY7eoXgQ4XUy02xna51PTsWPYANfzh36A5NY7KQrL+l23EnrWV8VgRyNCJ2s="; SPC_T_IV="beQldInTVFNRjcAxuMn3bg=="; SPC_R_T_IV="beQldInTVFNRjcAxuMn3bg=="; SPC_T_ID="h5sEB8bcl/05iuSfyphx4JGe1GU4SGMajYQKEeKMntGP8JaaY7eoXgQ4XUy02xna51PTsWPYANfzh36A5NY7KQrL+l23EnrWV8VgRyNCJ2s="',
        }
        
        params = (
            ('by', 'relevancy'),
            ('keyword', keyword),
            ('limit', '50'),
            ('newest', '0'),
            ('order', 'desc'),
            ('page_type', 'search'),
            ('version', '2'),
        )
        
        resp = requests.get('https://shopee.co.id/api/v2/search_items/', headers=headers, params=params)
        json_data = json.loads(resp.text)
        items = json_data['items']
        for item in items:
            images = item['images']
            item_rating = item['item_rating']

            shopid = item['shopid']
            itemid = item['itemid']

            review_count = 0
            if 'rating_count' in item_rating.keys() and item_rating['rating_count']:
                review_count = item_rating['rating_count'][0]

            data_to_write = OrderedDict()
            data_to_write['name'] = item['name'].strip()
            data_to_write['url'] = 'https://shopee.co.id/' + item['name'].strip().replace(' ', '-') + '-power-i.{}.{}'.format(str(shopid), str(itemid))
            if images:
                data_to_write['image_url'] = 'https://cf.shopee.co.id/file/' + item['image']
            else:
                data_to_write['image_url'] = ''
            data_to_write['rating'] = item_rating['rating_star']
            data_to_write['review_count'] = review_count
            data_to_write['price'] = item['price'] / 100000

            print('\t{}: '.format(str(total_count)) + data_to_write['url'])
            total_count += 1

            result_data_list.append(data_to_write)

        return result_data_list

class StudentsList(Resource):
    def get(self):
        parser.add_argument("keyword")
        args = parser.parse_args()
        response = getShopee(args["keyword"])
        return response
    

api.add_resource(StudentsList, '/api/')


if __name__ == "__main__":
    app.run(debug=True)
