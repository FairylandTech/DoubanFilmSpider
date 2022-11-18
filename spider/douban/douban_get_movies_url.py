# coding: utf8
""" 
@File: douban_get_movies_url.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 20:44
"""

import requests
from public.tb_create import CreateTables
from public.init_headers import BuildHeaders
import json
from public.tb_inster import InsterTables
import time, random


class SpiderDoubanMoviesInit(object):

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
        # response_status_code = response.status_code
        response_json = json.loads(response.content.decode())
        return response_json
    
    def save_movies_url(self, params):
        movies_details = self.douban_response_json(params=params).get('items')
        print(movies_details)
        if not movies_details:
            pass
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

    def batch_save_movies_url(self):
        CreateTables().c_tb_movies_simple_info()
        # types_list: list = [
        #     '喜剧', '爱情', '动作', '科幻', '动画', '悬疑', '犯罪', '惊悚', '冒险', '音乐', '历史', '奇幻', '恐怖', '战争', '传记', '歌舞', '武侠',
        #     '情色', '灾难', '西部', '纪录片', '短片'
        # ]
        types_list: list = [
            # '战争',
            # '情色', 
            '灾难', '西部', '纪录片', '短片'
        ]
        country_list: list = [
            '华语', '欧美', '韩国', '日本', '中国大陆', '美国', '中国香港', '中国台湾', '英国', '法国', '德国', '意大利', '西班牙', '印度', '泰国',
            '俄罗斯', '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦'
        ]
        for movies_type in types_list:
            selected_categories = json.dumps({"类型": f"{movies_type}"}, ensure_ascii=False)
            tags = f'{movies_type}'
            self.params.update(selected_categories=selected_categories, tags=tags)
            print(self.params)
            for start_num in range(0, 500, 20):
                self.params.update(start=f'{start_num}')
                print(self.params)
                self.save_movies_url(params=self.params)
                delay_time = random.randint(5, 10)
                print(delay_time)
                time.sleep(delay_time)
            for movies_country in country_list:
                selected_categories = json.dumps({"类型": f"{movies_type}", '地区': f'{movies_country}'}, ensure_ascii=False)
                tags = f'{movies_type},{movies_country}'
                self.params.update(selected_categories=selected_categories, tags=tags)
                print(self.params)
                for start_num in range(0, 500, 20):
                    self.params.update(start=f'{start_num}')
                    print(self.params)
                    self.save_movies_url(params=self.params)
                    delay_time = random.randint(5, 10)
                    print(delay_time)
                    time.sleep(delay_time)
                
    def test(self):
        # print(self.headers)
        response = self.douban_response_json().get('')
        print(response)
        pass
