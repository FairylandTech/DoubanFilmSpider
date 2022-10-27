# coding: utf8
"""
@File: main_test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 15:15
"""

import requests
import json
import fake_useragent
from lxml import etree
import re


class MoviesDouban(object):

    def __init__(self):
        self.headers = {
            'User-Agent': fake_useragent.UserAgent().random
        }

    def get_hot_movies(self):
        for number in range(0, 351, 50):
            request_url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={number}'
            response = requests.get(url=request_url, headers=self.headers)
            if response.status_code != 200:
                print('error')
                return False
            response_dict = json.loads(response.content.decode())
            resulDate = []
            for data in response_dict.get('subjects'):
                detailed_hot_movie_response = requests.request(
                    method='GET',
                    url=data['url'],
                    headers=self.headers,
                )
                parse_html = etree.HTML(detailed_hot_movie_response.content.decode())
                # 电影的导演
                detailed_hot_movie_director = parse_html.xpath('//span[@class="attrs"]/a[@rel="v:directedBy"]/text()')
                resulDate.append(','.join(detailed_hot_movie_director))
                # 电影评分
                detailed_hot_movie_rate = parse_html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong')
                resulDate.append(detailed_hot_movie_rate)
                # 电影的名称
                detailed_hot_movie_name = parse_html.xpath('//span[@property="v:itemreviewed"]/text()')
                resulDate.append(detailed_hot_movie_name)
                # 电影演员
                detailed_hot_movie_casts = parse_html.xpath('//*[@id="info"]/span[3]/span[2]')
                resulDate.append(','.join(detailed_hot_movie_casts))
                # 电影封面
                # 电影的详情链接
                detailed_hot_movie_url = data['url']
                resulDate.append(detailed_hot_movie_url)
                # 电影的年份
                detailed_hot_movie_year = re.search('\d'), parse_html.xpath('//*[@id="content"]/h1/span[2]/text()')[0].group()
                resulDate.append(detailed_hot_movie_year)
                # 电影类型
                detailed_hot_movie_types = []
                for i in parse_html.xpath('//*[@id="info"]/span[@property="v:genre"]'):
                    types.append(i.text)
                resulDate.append(','.json(detailed_hot_movie_types))
                # 电影国家
                textInfo = parse_html.xpath('//div[id="info"]/text()')
                detailed_hot__movie_country = []
                for i in textInfo:
                    if i.strip() and not i.strip() == "/":
                        detailed_hot__movie_country(i)
                resulDate.append(','.join(detailed_hot__movie_country[0].split(spa='/')))
                # 电影语言
                resulDate.append(','.join(detailed_hot__movie_country[1].split(spa='/')))
                # 电影上映时间
                print(resulDate)
                break

if __name__ == '__main__':
    MoviesDouban().get_hot_movies()