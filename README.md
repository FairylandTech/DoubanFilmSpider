# PublicDoubanMoviesDataSpider

豆瓣电影数据获取

[![author](https://img.shields.io/badge/Author-Alice-orange)](https://t.me/FairyAlicePro) [![github](https://img.shields.io/badge/Github-AliceEngineerPro-green)](https://github.com/AliceEngineerPro) [![github](https://img.shields.io/badge/GitBook-AliceEngineerProGitBook-green)](https://interestingbooks.gitbook.io/) [![type](https://img.shields.io/badge/Type-Project-blue)](https://github.com/AliceEngineerPro) [![editor](https://img.shields.io/badge/Editor-Typora-yellow)](https://github.com/AliceEngineerPro) [![file](https://img.shields.io/badge/Language-Python3.9.13-orange)](https://github.com/AliceEngineerPro) [![version](https://img.shields.io/badge/Version-Release-blue)](https://github.com/AliceEngineerPro) [![docs](https://img.shields.io/badge/Docs-Passing-brightgreen)](https://github.com/AliceEngineerPro) [![License](https://img.shields.io/badge/License-GNU_Version3-green)](./LICENSE) [![](https://img.shields.io/badge/%E7%AD%89%E6%88%91%E4%BB%A3%E7%A0%81%E7%BC%96%E6%88%90-%E5%A8%B6%E4%BD%A0%E4%B8%BA%E5%A6%BB%E5%8F%AF%E5%A5%BD@-red)](https://github.com/AliceEngineerPro) 

## 一. 项目介绍

批量获取豆瓣网站电影数据，根据简单分类存入数据库（MySQL）

## 二. 项目运行

### 1. 下载代码：

- git clone

```shell
git clone
```

### 2. 安装依赖

```shell
pip install -r requirements.txt
```

### 3. 更新配置文件(yaml文件)

### 4. 启动项目

## 三. 问题反馈

任何问题欢迎在Issues中反馈

你的反馈会让此项目变得更加完美。

## 四. 贡献代码

本项目依然不够完善，如果发现bug或有新的功能添加，请在Issues中提交bug、新功能描述，我会尽力改进，使她更加完美。

## 五.数据获取说明

1. 识别豆瓣电影数据的如何展示到web页面上的(一种是通过API(直接请求API(一般使用get方式来请求数据,要明确get传入了什么值),页面渲染)
2. 如果是API的形式就直接请求这个接口(获取到json的值来转为python中的字典(dict)再来做二次处理); 如果是页面渲染来获取值, 那么就要请求这个web页面来解析html来根据页面上的标签来获取值(假如你要获取一个图片或者视频的URL,那么就要通过Xpath或bs4来找到这个`a`标签来获取`a`标签中的`value`值
3. 该项目第一步是来获取电影详情页面URL以及电影的名称(API)
4. 把`电影详情页面URL`以及`电影名`存入设计好的数据表
5. 通过来请求第一次获取(要从数据库中查询)到的`电影详情URL地址`来获取该电影的详细数据(导演,演员,时长,评分等)(页面渲染);(bs4, re)来组装拼接过滤筛选自己所需要的字段值
6. 获取电影需要的字段值存入设计好的数据表中

## 六.数据简单清洗说明

1. 单字段分组查询后来判断查询结构是否符合该字段的定义

## Release Notes

[AliceEngineer](https://github.com/AliceEngineerPro) 

