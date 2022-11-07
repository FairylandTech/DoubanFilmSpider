# coding: utf8
""" 
@File: douban_spider_data.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 20:44
"""

import requests
from spider.public.tb_create import CreateTables
from spider.public.init_headers import BuildHeaders
import json
from spider.public.tb_inster import InsterTables


class SpiderDoubanMoviesDatas(object):

    def __init__(self):
        CreateTables().c_tb_movies_temp_info()
        self.url = 'https://m.douban.com/rexxar/api/v2/movie/recommend'
        self.movies_details_url = 'https://movie.douban.com/subject'
        self.headers = BuildHeaders.headers()
        self.proxies = {
            'http': 'http://127.0.0.1:65353',
            'https': 'http://127.0.0.1:65353',
            # 'sock': 'socks5://127.0.0.1:65353'
        }
        self.cookies = {
            "ll": "118318",
            "bid": "DcI5Fbd5RAQ",
            "ap_v": "0,6.0",
            "dbcl2": "264064658:Eb5fqV+OILA",
            "ck": "F6Lh",
            "push_noty_num": "0",
            "push_doumail_num": "0",
            "frodotk": "2631c3e438ad25a472954bacaa0770ec"
        }
        self.params = {
            "refresh": "0",
            "start": "0",
            "count": "20",
            # "selected_categories": "%7B%7D",
            "selected_categories": "{}",
            "uncollect": "false",
            "tags": "",
            "ck": self.cookies.get('ck')
        }

    def douban_response_json(self, params) -> dict:
        response = requests.request(
            method='GET',
            url=self.url,
            headers=self.headers,
            params=params,
            cookies=self.cookies,
        )
        response_json = json.loads(response.content.decode())
        return response_json
    
    def douban_movies_details(self, params):
        movies_details = self.douban_response_json(params=params).get('items')
        for index, details in enumerate(movies_details):
            index: int
            details: dict
            try:
                id: str = details.get('id')
                title: str = details.get('title')
                data_type: str = details.get('type')
                if id.isdigit() and data_type == 'movie':
                    url = self.movies_details_url + f'/{id}'
                    print('{}, {}'.format(title, url))
                    InsterTables().insert_tb_movies_simple_info(title=title, url=url)
                else:
                    pass
            except Exception as error:
                print(index, error)
                pass
            

    def test(self):
        # print(self.headers)
        response = self.douban_response_json().get('')
        print(response)
        pass
