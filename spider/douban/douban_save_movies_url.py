# coding: utf8
""" 
@File: douban_save_movies_url.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 23:36
"""

from spider.douban.douban_spider_data import SpiderDoubanMoviesDatas
from spider.public.tb_create import CreateTables
import time, random, json

class BatchedSpiderDoubanMoviesDatas(SpiderDoubanMoviesDatas):
    
    def batch_datas(self, end_num=500, movies_type=None):
        CreateTables().c_tb_movies_simple_info()
        if movies_type is None:
            pass
        else:
            selected_categories = json.dumps({"类型": f"{movies_type}"}, ensure_ascii=False)
            tags = f'{movies_type}'
            self.params.update(selected_categories=selected_categories, tags=tags)
        for start_num in range(0, end_num, 20):
            self.params.update(start=f'{start_num}')
            print(self.params)
            self.douban_movies_details(params=self.params)
            delay_time = random.randint(5, 10)
            print(delay_time)
            time.sleep(delay_time)
            
    def douban_movies_types(self):
        types_list: list = [
            '喜剧', '爱情', '动作', '科幻', '动画', '悬疑', '犯罪', '惊悚', '冒险', '音乐', '历史', '奇幻', '恐怖', '战争', '传记', '歌舞', '武侠',
            '情色', '灾难', '西部', '纪录片', '短片'
        ]
        country_list: list = [
            '华语', '欧美', '韩国', '日本', '中国大陆', '美国', '中国香港', '中国台湾', '英国', '法国', '德国', '意大利', '西班牙', '印度', '泰国',
            '俄罗斯', '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦'
        ]
        time_list: list = [
            
        ]
        for movies_type in types_list:
            selected_categories = json.dumps({"类型": f"{movies_type}"}, ensure_ascii=False)
            tags = f'{movies_type}'
            self.params.update(selected_categories=selected_categories, tags=tags)
            print(self.params)
            for movies_country in country_list:
                selected_categories = json.dumps({"类型": f"{movies_type}", '地区': f'{movies_country}'}, ensure_ascii=False)
                tags = f'{movies_type},{movies_country}'
                self.params.update(selected_categories=selected_categories, tags=tags)
                print(self.params)
        
