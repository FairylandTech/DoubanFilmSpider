# coding: utf8
""" 
@File: douban_test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/8 11:46
"""

from bs4 import BeautifulSoup
import re, json
import requests

douban_html = """<!DOCTYPE html>
<html lang="zh-CN" class="ua-linux ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        独行月球 (豆瓣)
</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/204847ecc7d679de915c283531d14f16cfbee65e/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/0b4cdb02dd620693709d9314196b617f17c2f9ea/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/252bef058b97005c6a41e8f1b9f7b06b84bc71b3/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/4888ee2fda6812f70a064a51c93b84fde8e4a3c2/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/b0d3faaf7a432605add54908e39e17746824d6cc/js/separation/_all.js"></script>
    
    <meta name="keywords" content="独行月球,独行月球,独行月球影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="独行月球电影简介和剧情介绍,独行月球影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/movie/subject/35183042/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/35183042/" />
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/2c0c1c6b83f9a457b0f38c38a32fc43a42ec9bad/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>
    
  <script type='text/javascript'>
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>


    


<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "name": "独行月球",
  "url": "/subject/35183042/",
  "image": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg",
  "director": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1381643/",
      "name": "张吃鱼 Chiyu Zhang"
    }
  ]
,
  "author": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1381643/",
      "name": "张吃鱼 Chiyu Zhang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1388864/",
      "name": "钱晨光 Chenguang Qian"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1439105/",
      "name": "戴思奥 Si&#39;ao Dai"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1439106/",
      "name": "沈雨悦 Yuyue Shen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1475456/",
      "name": "赵石 Seok Jo "
    }
  ]
,
  "actor": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1325700/",
      "name": "沈腾 Teng Shen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1319032/",
      "name": "马丽 Li Ma"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1327084/",
      "name": "常远 Yuan Chang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1314331/",
      "name": "李诚儒 Chengru Li"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1363857/",
      "name": "黄才伦 Cailun Huang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1381644/",
      "name": "李嘉琦 Jackie Li"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1432508/",
      "name": "郝瀚 Han Hao"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1337445/",
      "name": "黄子韬 Zitao Huang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1383525/",
      "name": "王成思 Chengsi Wang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1394939/",
      "name": "高海宝 Haibao Gao"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1475378/",
      "name": "杨铮 Zheng Yang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1342395/",
      "name": "史彭元 Pengyuan Shi"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1425470/",
      "name": "张熙然 Xiran Zhang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1326050/",
      "name": "黄品沅 Ruomeng Huang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1318482/",
      "name": "杨皓宇 Haoyu Yang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1461262/",
      "name": "徐志胜 Zhisheng Xu"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1351815/",
      "name": "杜晓宇 Xiaoyu Du"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1407469/",
      "name": "李海银 Haiyin Li"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1353283/",
      "name": "陶亮 Liang Tao"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1398189/",
      "name": "王赞 Zan Wang"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1381397/",
      "name": "李唯贺 Weihe Li"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1344888/",
      "name": "陈昊明 Haoming Chen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1407772/",
      "name": "孟芷旭 Zhixu Meng"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1406908/",
      "name": "赵一霖 Yilin Zhao"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1480042/",
      "name": "吴培郡 Peijun Wu"
    }
  ]
,
  "datePublished": "2022-07-29",
  "genre": ["\u559c\u5267", "\u79d1\u5e7b"],
  "duration": "PT2H2M",
  "description": "人类为抵御小行星的撞击，拯救地球，在月球部署了月盾计划。陨石提前来袭，全员紧急撤离时，维修工独孤月（沈腾 饰）因为意外，错过了领队马蓝星（马丽 饰）的撤离通知，一个人落在了月球。不料月盾计划失败，独孤...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "563783",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "6.7"
  }
}
</script>

    
    
    <meta property="og:title" content="独行月球" />
    <meta property="og:description" content="人类为抵御小行星的撞击，拯救地球，在月球部署了月盾计划。陨石提前来袭，全员紧急撤离时，维修工独孤月（沈腾 饰）因为意外，错过了领队马蓝星（马丽 饰）的撤离通知，一个人落在了月球。不料月盾计划失败，独孤..." />
    <meta property="og:site_name" content="豆瓣" />
    <meta property="og:url" content="https://movie.douban.com/subject/35183042/" />
    <meta property="og:image" content="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg" />
    <meta property="og:type" content="video.movie" />
            <meta property="video:actor" content="沈腾" />
            <meta property="video:actor" content="马丽" />
            <meta property="video:actor" content="常远" />
            <meta property="video:actor" content="李诚儒" />
            <meta property="video:actor" content="黄才伦" />
            <meta property="video:actor" content="李嘉琦" />
            <meta property="video:actor" content="郝瀚" />
            <meta property="video:actor" content="黄子韬" />
            <meta property="video:actor" content="王成思" />
            <meta property="video:actor" content="高海宝" />
            <meta property="video:actor" content="杨铮" />
            <meta property="video:actor" content="史彭元" />
            <meta property="video:actor" content="张熙然" />
            <meta property="video:actor" content="黄品沅" />
            <meta property="video:actor" content="杨皓宇" />
            <meta property="video:actor" content="徐志胜" />
            <meta property="video:actor" content="杜晓宇" />
            <meta property="video:actor" content="李海银" />
            <meta property="video:actor" content="陶亮" />
            <meta property="video:actor" content="王赞" />
            <meta property="video:actor" content="李唯贺" />
            <meta property="video:actor" content="陈昊明" />
            <meta property="video:actor" content="孟芷旭" />
            <meta property="video:actor" content="赵一霖" />
            <meta property="video:actor" content="吴培郡" />
            <meta property="video:director" content="张吃鱼" />
        <meta property="video:duration" content="7320" />


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/73294e97a1a89e46.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/3e96b44/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <ul>
    <li>
    <a id="top-nav-doumail-link" href="https://www.douban.com/doumail/">豆邮</a>
    </li>
    <li class="nav-user-account">
      <a target="_blank" href="https://accounts.douban.com/passport/setting/" class="bn-more">
        <span>AliceEngineer的帐号</span><span class="arrow"></span>
      </a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://www.douban.com/mine/">个人主页</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/orders/">我的订单</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/wallet/">我的钱包</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://accounts.douban.com/passport/setting/">帐号管理</a>
              </td>
            </tr>
            <tr>
              <td>
                <a href="https://www.douban.com/accounts/logout?source=movie&ck=F6Lh">退出</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  <div class="top-nav-reminder">
    <a href="https://www.douban.com/notification/" class="lnk-remind">提醒</a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
        <p>加载中...</p>
      </div>
    </div>
  </div>

    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;264064658&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;264064658&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;264064658&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;264064658&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;264064658&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;264064658&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;264064658&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;264064658&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;264064658&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;264064658&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    USER_ID: "264064658",
    UPLOAD_AUTH_TOKEN: "264064658:caa26b00fdbc4f55c0cb37f0f627f2127c8822d5",
    SSE_TOKEN: "1f756733671e5b559a57f76b53ea18bb5ea153bc",
    SSE_TIMESTAMP: "1667882920",
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/3e96b44/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/3e96b44/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;search.douban.com&#47;movie/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/mine"
     >我看</a>
    </li>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual/2021?source=navigation"
     >2021年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2021?fullscreen=true&hidenav=true&autorotate=false&source=movie_navigation"
            target="_blank"
     >2021书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2021?source=movie_navigation" class="movieannual"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/3e96b44/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">独行月球</span>
            <span class="year">(2022)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">
                    
                        



<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/35183042/photos?type=R" title="点击看更多海报">
        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg" title="点击看更多海报" alt="独行月球" rel="v:image" />
   </a>
                <p class="gact">
                    <a href="https://movie.douban.com/subject/35183042/edit">
                        更新描述或海报
                    </a>
                </p>
</div>

                    


<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1381643/" rel="v:directedBy">张吃鱼</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1381643/">张吃鱼</a> / <a href="/celebrity/1388864/">钱晨光</a> / <a href="/celebrity/1439105/">戴思奥</a> / <a href="/celebrity/1439106/">沈雨悦</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1325700/" rel="v:starring">沈腾</a> / <a href="/celebrity/1319032/" rel="v:starring">马丽</a> / <a href="/celebrity/1327084/" rel="v:starring">常远</a> / <a href="/celebrity/1314331/" rel="v:starring">李诚儒</a> / <a href="/celebrity/1363857/" rel="v:starring">黄才伦</a> / <a href="/celebrity/1381644/" rel="v:starring">李嘉琦</a> / <a href="/celebrity/1432508/" rel="v:starring">郝瀚</a> / <a href="/celebrity/1337445/" rel="v:starring">黄子韬</a> / <a href="/celebrity/1383525/" rel="v:starring">王成思</a> / <a href="/celebrity/1394939/" rel="v:starring">高海宝</a> / <a href="/celebrity/1475378/" rel="v:starring">杨铮</a> / <a href="/celebrity/1342395/" rel="v:starring">史彭元</a> / <a href="/celebrity/1425470/" rel="v:starring">张熙然</a> / <a href="/celebrity/1326050/" rel="v:starring">黄品沅</a> / <a href="/celebrity/1318482/" rel="v:starring">杨皓宇</a> / <a href="/celebrity/1461262/" rel="v:starring">徐志胜</a> / <a href="/celebrity/1351815/" rel="v:starring">杜晓宇</a> / <a href="/celebrity/1407469/" rel="v:starring">李海银</a> / <a href="/celebrity/1353283/" rel="v:starring">陶亮</a> / <a href="/celebrity/1398189/" rel="v:starring">王赞</a> / <a href="/celebrity/1381397/" rel="v:starring">李唯贺</a> / <a href="/celebrity/1344888/" rel="v:starring">陈昊明</a> / <a href="/celebrity/1407772/" rel="v:starring">孟芷旭</a> / <a href="/celebrity/1406908/" rel="v:starring">赵一霖</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">喜剧</span> / <span property="v:genre">科幻</span><br/>
        
        <span class="pl">制片国家/地区:</span> 中国大陆<br/>
        <span class="pl">语言:</span> 汉语普通话 / 英语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2022-07-29(中国大陆)">2022-07-29(中国大陆)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="122">122分钟</span><br/>
        <span class="pl">又名:</span> Moon Man<br/>
        <span class="pl">IMDb:</span> tt14557302<br>

</div>




                </div>
                
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
            <div class="rating_logo ll">
                豆瓣评分
            </div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">6.7</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar35"></div>
        <div class="rating_sum">
                <a href="comments" class="rating_people">
                    <span property="v:votes">563784</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:16px"></div>
        <span class="rating_per">10.8%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:46px"></div>
        <span class="rating_per">31.1%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">43.1%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:17px"></div>
        <span class="rating_per">11.8%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:4px"></div>
        <span class="rating_per">3.2%</span>
        <br />
        </div>
</div>

    </div>
        
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=喜剧&type=24&interval_id=85:75&action=">81% 喜剧片</a><br/>
            好于 <a href="/typerank?type_name=科幻&type=17&interval_id=80:70&action=">79% 科幻片</a><br/>
        </div>
</div>


                
            </div>
            
                





<div id="interest_sect_level" class="clearfix">
        
            <a href="https://movie.douban.com/subject/35183042/?interest=wish&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-35183042-wish">
                <span>想看</span>
            </a>
            <a href="https://movie.douban.com/subject/35183042/?interest=collect&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-35183042-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-35183042-collect-1">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-35183042-collect-2">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-35183042-collect-3">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-35183042-collect-4">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-35183042-collect-5">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/>
        </a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>
    

</div>


            

















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                
                  <li> 
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt'})" href="javascript:;" class="j a_collect_btn" name="cbtn-35183042">写短评</a>
 </li>
                  <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv'})" class="cls_abnormal" href="https://movie.douban.com/subject/35183042/new_review" rel="nofollow">写影评</a>
 </li>
                    <li> 
        


  <link rel="stylesheet" href="https://img3.doubanio.com/f/sns/9919c071eab1c25bc462d58a582feb79e3867be4/css/sns/doulist/new_doulist_button.css">
    <div class="doulist-add-btn">

  

  
  <a href="javascript:void(0)"
     data-id="35183042"
     data-cate="1002"
     data-canview="True"
     data-url="https://movie.douban.com/subject/35183042/"
     data-catename="电影"
     data-link="https://www.douban.com/people/264064658/doulists/all?add=35183042&amp;cat=1002"
     data-title="独行月球"
     data-picture="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg"
     class="lnk-doulist-add"
     onclick="moreurl(this, { 'from':'doulist-btn-1002-35183042-264064658'})">
      <i></i>添加到片单
  </a>
    </div>
  <link rel="stylesheet" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css">
  <script src="https://img3.doubanio.com/f/shire/3f6bfbf287470b91aacba40f0b19cb2056910f2e/js/core/do/loader.js"></script>
  <script src="https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js"></script>
  <script>
    Do(function() {
      loader.batch([
        "https://img3.doubanio.com/f/sns/339d5de8cb2b7ac836b834518bc33260e83e0a79/js/sns/doulist/doulist_dialog.js",
      ]).done(function() {
        $(document).delegate('.lnk-doulist-add', 'click', function(e) {
          e.preventDefault();
          var self = $(this);
          if(window._USER_ABNORMAL) {
            show_abnormal && show_abnormal()
            return
          }
          var param = $.extend({'url':''}, $(this).data(), {link: this.href});
          // 兼容jquery 1.8.x
          var newParam = {};
          for (key in param) {
            if (typeof param[key] === 'number') {
              param[key] = self.attr('data-'+key);
            }
            if (param.hasOwnProperty(key)) {
              newParam[$.camelCase(key)] = param[key];
            }
          }
          self.doulistDialog(newParam);
        });

      });
    });
  </script>

 </li>
                    <li> 
   

   
    
    <span class="rec" id="电影-35183042">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/35183042/"
        data-desc="电影《独行月球》 (来自豆瓣) "
        data-title="电影《独行月球》 (来自豆瓣) "
        data-pic="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpeg"
        class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img3.doubanio.com/f/movie/09f0f3e441f00f6d89e35b4c29ed1ad5b4f2d191/js/movie/lib/sharebutton.js');
    </script>


  </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
        });
    </script>
</div>




            
                




        <script type="text/javascript">
            Do.add('dialog-css', {path: "https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css",
                type: 'css'})
            Do.add('dialog', {path: "https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js", type: 'js',
                requires: ['dialog-css']})
            Do.add('textarea-mention-default-style', {
                path: "https://img3.doubanio.com/f/shire/887858ba20379f8a4789863ea7fda9a6ef36a0e5/css/lib/textarea-mention.css", type: 'css'})
            Do.add('textarea-mention', {
                path: "https://img3.doubanio.com/f/shire/3213351df629ca402ae8f0e1494b16b2011d8a73/js/lib/textarea-mention.js", type: 'js',
                requires: ['mustache', 'textarea-mention-default-style']})
            Do.add('mustache', {path: "https://img3.doubanio.com/f/shire/e0d80c43c73e241e9f218387d74a3e800d31179f/js/lib/mustache.js", type: 'js'})
            Do.add('movie-share-css', {path: "https://img3.doubanio.com/f/movie/6ab3b78c54165a03a932babd615d11fcdbfce2a3/css/movie/share.css",
                type: 'css'})
            Do.add('movie:share', {path: "https://img3.doubanio.com/f/movie/230795bbf6a9a7700cc6f395067493d5dcc572ad/js/movie/share.js", type: 'js',
                requires: ['dialog', 'textarea-mention', 'movie-share-css']})
            Do('movie:share')
        </script>

<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">
        
    <form class="movie-share" action="/j/share" method="POST"><div style="display:none;"><input type="hidden" name="ck" value="F6Lh"/></div>
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="35183042">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="独行月球‎ (2022)">
                <input type="hidden" name="desc" value="导演 张吃鱼 主演 沈腾 / 马丽 / 中国大陆 / 6.7分(563784评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg" />
                <strong>独行月球‎ (2022)</strong>
                <p>导演 张吃鱼 主演 沈腾 / 马丽 / 中国大陆 / 6.7分(563784评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">
                




<div class="sync-setting pl">
    <label>分享到</label>
    <label class="share-label share-shuo" for="share-shuo">
        
            <input id="share-shuo" name="share-shuo" value="douban" type="checkbox" checked="checked" />豆瓣广播
    </label>



            <a id="lnk-sync-setting" class="no-visited no-hover" href="https://movie.douban.com/settings/sync" target="_blank"
                class="pl share-label"><img src="https://img3.doubanio.com/f/movie/9389c4e5cab0cd1089a189d607d296c31ddb1bc0/pics/movie/share_g.png"
                alt="去绑定新浪微博" />去绑定新浪微博</a>

</div>

<style type="text/css">
    .sync-setting {
        float: left;
    }
    #lnk-sync-setting,
    #lnk-sync-setting:hover,
    #lnk-sync-setting:visited {
        vertical-align: middle;
        color: #0192b5;
        background: none;
        line-height: 27px;
        margin-right: 8px;
    }
    #lnk-sync-setting img {
        vertical-align: baseline;
        *vertical-align: middle;
        opacity: .5;
        filter: alpha(opacity=50);
        display: inline-block;
        width: 10px;
        height: 10px;
        *display: inline;
        zoom: 1;
        position: relative;
        top: 1px;
        margin-left: 5px;
    }
    #lnk-sync-setting:hover img {
        opacity: .8;
        background: none;
        filter: alpha(opacity=80);
    }
    .share-label {
        margin: 8px;
        cursor: pointer;
        vertical-align: middle;
        *vertical-align: text-bottom;
    }
    .interest-form-ft .share-label input {
        margin-bottom: 0;
    }
    .interest-form-ft {
        text-align: right;
    }
    .interest-form-ft .bn-flat {
        float: none;
    }
    .interest-form-ft .sync-setting {
        float: left;
        line-height: 25px;
    }
</style>


                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>
    
    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>

        
        <a href="#" data-share-dialog="#movie-share" data-dialog-title="推荐电影" class="cls_abnormal lnk-sharing" 
            share-id="35183042" 
            data-mode="plain" data-name="独行月球‎ (2022)" 
            data-type="movie" data-desc="导演 张吃鱼 主演 沈腾 / 马丽 / 中国大陆 / 6.7分(563784评价)" 
            data-href="https://movie.douban.com/subject/35183042/" data-image="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2876409008.jpg" 
            data-properties="{}" 
            data-redir="" data-text="" 
            data-apikey="" data-curl="" 
            data-count="10" data-object_kind="1002" 
            data-object_id="35183042" data-target_type="rec" 
            data-target_action="0" 
            data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/35183042\/&#34;,&#34;subject_title&#34;:&#34;独行月球‎ (2022)&#34;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_35183042"></div>


        



<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">独行月球的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report-intra">
                    
                        <span property="v:summary" class="">
                                　　人类为抵御小行星的撞击，拯救地球，在月球部署了月盾计划。陨石提前来袭，全员紧急撤离时，维修工独孤月（沈腾 饰）因为意外，错过了领队马蓝星（马丽 饰）的撤离通知，一个人落在了月球。不料月盾计划失败，独孤月成为了“宇宙最后的人类”，开始了他在月球上破罐子破摔的生活……
                        </span>
                        <div class="clear"></div>
                        
  <link rel="stylesheet" href="https://img3.doubanio.com/f/vendors/7d8c54c10ffd51769880282d4a41609dc465b796/reports.css" />
  <style>
    .btn-report { float: right; color: #bbb; cursor: pointer; font-size: 13px; }
  </style>
  <script src="https://img3.doubanio.com/f/vendors/bd6325a12f40c34cbf2668aafafb4ccd60deab7e/vendors.js"></script>
  <script src="https://img3.doubanio.com/f/vendors/68e2c291c7d4971661f7e4c3e41e1e99e2c2df4b/reports.js"></script>
  <script>
    (function () {
      var ADD_REPORT = function() {
        var roots = document.querySelectorAll("#link-report-intra");
        roots.forEach(function (root) {
          var btn = document.createElement('span');
          btn.className = 'btn-report';
          btn.innerHTML = "投诉";
          btn.addEventListener('click', function () {
            if (window.DOUBAN_VENDORS && window.DOUBAN_VENDORS.openReportModal) {
              window.DOUBAN_VENDORS.openReportModal({
                reportUrl: "https://movie.douban.com/subject/35183042/" || root.getAttribute('data-url'),
                types: ["content"]
              })
            }
          });
          root.appendChild(btn);
        })
      }
      ADD_REPORT();
      window.ADD_REPORT = ADD_REPORT;
    })()
  </script>

            </div>
</div>


    <div id="dale_movie_subject_banner_after_intro"></div>

    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">独行月球的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/35183042/celebrities">全部 45</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1381643/" title="张吃鱼 Chiyu Zhang" class="has-account">
      <div class="avatar has-account" style="background-image: url(https://img3.doubanio.com/f/movie/14960825e118267b5857fc0ae9f306ef8c74da8f/pics/movie/has_douban@2x.png), url(https://img2.doubanio.com/view/personage/raw/public/59f123cd5e5587c9d2feee62952dd902.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1381643/" title="张吃鱼 Chiyu Zhang" class="name">张吃鱼</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1325700/" title="沈腾 Teng Shen" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/personage/raw/public/48cd3ad8de4fe3635023a831b84ceb88.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1325700/" title="沈腾 Teng Shen" class="name">沈腾</a></span>

      <span class="role" title="饰 独孤月">饰 独孤月</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1319032/" title="马丽 Li Ma" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/personage/raw/public/3e7d8a0937da82965aadb300a6b9a227.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1319032/" title="马丽 Li Ma" class="name">马丽</a></span>

      <span class="role" title="饰 马蓝星">饰 马蓝星</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1327084/" title="常远 Yuan Chang" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/personage/raw/public/ca4e7cdbe19c1ab56d60cc19b50fe918.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1327084/" title="常远 Yuan Chang" class="name">常远</a></span>

      <span class="role" title="饰 朱皮特">饰 朱皮特</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1314331/" title="李诚儒 Chengru Li" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/personage/raw/public/0af5455ca38894bc4fc9631c6e3287a8.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1314331/" title="李诚儒 Chengru Li" class="name">李诚儒</a></span>

      <span class="role" title="饰 孙光阳">饰 孙光阳</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1363857/" title="黄才伦 Cailun Huang" class="">
      <div class="avatar" style="background-image: url(https://img9.doubanio.com/view/personage/raw/public/723633f33aeec16bae569c05b9bacc55.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1363857/" title="黄才伦 Cailun Huang" class="name">黄才伦</a></span>

      <span class="role" title="饰 葫芦丝儿">饰 葫芦丝儿</span>

    </div>
  </li>


  </ul>
</div>


    


<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/fada435abd10ae2583d995730a9e06e6e20a9a05/entry_creator/dist/author_subject/style.css">
<div id="author_subject" class="author-wrapper">
    <div class="loading"></div>
</div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '35183042',
      USER_ID: '264064658'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/82d2333c56fe1813ad6ee312f35a915941d906ae/entry_creator/dist/author_subject/index.js"></script>


    
        










    
    <div id="related-pic" class="related-pic">
        
    
    
    <h2>
        <i class="">独行月球的视频和图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/35183042/trailer#trailer">预告片16</a>&nbsp;|&nbsp;<a href="/video/create?subject_id=35183042">添加视频评论</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/35183042/all_photos">图片572</a>&nbsp;·&nbsp;<a href="https://movie.douban.com/subject/35183042/mupload">添加</a>
            )
            </span>
    </h2>


        <ul class="related-pic-bd  ">
                <li class="label-trailer">
                    <a class="related-pic-video" href="https://movie.douban.com/trailer/292596/#content" title="预告片" style="background-image:url(https://img2.doubanio.com/img/trailer/medium/2876823872.jpg?)">
                    </a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2876606695/"><img src="https://img9.doubanio.com/view/photo/sqxs/public/p2876606695.jpg" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2876589600/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2876589600.jpg" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2876606698/"><img src="https://img1.doubanio.com/view/photo/sqxs/public/p2876606698.jpg" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2876589602/"><img src="https://img2.doubanio.com/view/photo/sqxs/public/p2876589602.jpg" alt="图片" /></a>
                </li>
        </ul>
    </div>



    

    



<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>




    
        








    <div id="recommendations" class="">
        
        
    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>

        
    
    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/35505100/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2814949620.jpg" alt="这个杀手不太冷静" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/35505100/?from=subject-page" class="" >这个杀手不太冷静</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/27038183/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2499793218.jpg" alt="羞羞的铁拳" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/27038183/?from=subject-page" class="" >羞羞的铁拳</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/35069506/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2621101922.jpg" alt="一点就到家" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/35069506/?from=subject-page" class="" >一点就到家</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/27605698/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529206747.jpg" alt="西虹市首富" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/27605698/?from=subject-page" class="" >西虹市首富</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/35051512/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2620453443.jpg" alt="我和我的家乡" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/35051512/?from=subject-page" class="" >我和我的家乡</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/34869362/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2618446242.jpg" alt="温暖的抱抱" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/34869362/?from=subject-page" class="" >温暖的抱抱</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25964071/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2264377763.jpg" alt="夏洛特烦恼" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25964071/?from=subject-page" class="" >夏洛特烦恼</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/34894753/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627788612.jpg" alt="沐浴之王" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/34894753/?from=subject-page" class="" >沐浴之王</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/30337388/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2677520025.jpg" alt="失控玩家" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/30337388/?from=subject-page" class="" >失控玩家</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25986662/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2541901817.jpg" alt="疯狂的外星人" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25986662/?from=subject-page" class="" >疯狂的外星人</a>
            </dd>
        </dl>
    </div>

    </div>



    
        



<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}vote-comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content_tmpl content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>












    

    <div id="comments-section">
        <div class="mod-hd">
            
            
        <a class="comment_btn j a_collect_btn" name="cbtn-35183042" href="javascript:;" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">独行月球的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/35183042/comments?status=P">全部 253986 条</a>
            )
            </span>
    </h2>

        </div>
       
        


        <div class="mod-bd">
                
        <div class="tab-hd">
                        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
                        <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
                        <a id="following-comments-tab" href="comments?sort=follows" data-id="following" >好友</a>
        </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    

        
        <div class="comment-item " data-cid="3437901813">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">6933</span>

                    <input value="3437901813" type="hidden"/>
                    <a href="javascript:;" data-id="3437901813"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/52889164/" class="">看電影的人</a>
                    <span>看过</span>
                    <span class="allstar20 rating" title="较差"></span>
                <span class="comment-time " title="2022-07-29 11:05:42">
                    2022-07-29 11:05:42
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">笑'不出'来.gif</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/35183042/?comment_id=3437901813"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="3438260632">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">8690</span>

                    <input value="3438260632" type="hidden"/>
                    <a href="javascript:;" data-id="3438260632"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/hfeifei1010/" class="">柒初柒</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2022-07-29 11:26:57">
                    2022-07-29 11:26:57
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">这么说吧，光想到人类唯一的幸存者是沈腾就感觉很好笑</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/35183042/?comment_id=3438260632"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="3437733663">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">15172</span>

                    <input value="3437733663" type="hidden"/>
                    <a href="javascript:;" data-id="3437733663"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/69575176/" class="">绝望的生鱼片</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2022-07-29 12:14:20">
                    2022-07-29 12:14:20
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">我非常讨厌往喜剧片里塞煽情的部分，导致我从后半段就几乎笑不出来了，煽情塞进喜剧片里适配度很差</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/35183042/?comment_id=3437733663"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="3438242981">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">7491</span>

                    <input value="3438242981" type="hidden"/>
                    <a href="javascript:;" data-id="3438242981"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/157194387/" class="">Bei</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2022-07-29 11:07:35">
                    2022-07-29 11:07:35
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">太他妈的浪漫了。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/35183042/?comment_id=3438242981"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="3438262486">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">5243</span>

                    <input value="3438262486" type="hidden"/>
                    <a href="javascript:;" data-id="3438262486"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/rayland/" class="">壹安²</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2022-07-29 11:28:57">
                    2022-07-29 11:28:57
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">磕幻喜剧哈哈哈哈哈哈，我竟然磕到了沈马这两张老脸？最后…沈腾炸的是国产科幻封了3年的大门。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/35183042/?comment_id=3438262486"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>




                
                    &gt; <a href="comments?sort=new_score&status=P" >
                        更多短评
                            253986条
                    </a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    




        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>
    
  <link rel="stylesheet" href="https://img3.doubanio.com/f/vendors/7d8c54c10ffd51769880282d4a41609dc465b796/reports.css" />
  <style>
    .btn-report { float: right; color: #bbb; cursor: pointer; font-size: 13px; }
  </style>
  <script src="https://img3.doubanio.com/f/vendors/bd6325a12f40c34cbf2668aafafb4ccd60deab7e/vendors.js"></script>
  <script src="https://img3.doubanio.com/f/vendors/68e2c291c7d4971661f7e4c3e41e1e99e2c2df4b/reports.js"></script>
  <script>
    (function () {
      var ADD_REPORT = function() {
        var roots = document.querySelectorAll(".comment-report");
        roots.forEach(function (root) {
          var btn = document.createElement('span');
          btn.className = 'btn-report';
          btn.innerHTML = "投诉";
          btn.addEventListener('click', function () {
            if (window.DOUBAN_VENDORS && window.DOUBAN_VENDORS.openReportModal) {
              window.DOUBAN_VENDORS.openReportModal({
                reportUrl: "" || root.getAttribute('data-url'),
                types: ["content"]
              })
            }
          });
          root.appendChild(btn);
        })
      }
      ADD_REPORT();
      window.ADD_REPORT = ADD_REPORT;
    })()
  </script>



            
            
        </div>
    </div>



<!--        此处是挂载其他页面，不是注释！不是注释！不是注释！-->
        


<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/6078555e83c38f2.css">

    <section id="reviews-wrapper" class="reviews mod movie-content">
        <header>
            
                <a href="new_review" rel="nofollow" class="create-review comment_btn cls_abnormal"
                    data-isverify="True"
                    data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/35183042/new_review">
                    <span>我要写影评</span>
                </a>
            <h2>
                    独行月球的影评 · · · · · ·

                    <span class="pl">( <a href="reviews">全部 3420 条</a> )</span>
            </h2>
        </header>

            <div class="review_filter">
                            <a href="javascript:;;" class="cur" data-sort="">热门</a> &#047;
                            <a href="javascript:;;" data-sort="time">最新</a> &#047;
                            <a href="javascript:;;" data-sort="follow">好友</a>
            </div>
            <script>
                var cur_sort = '';
                $('#reviews-wrapper .review_filter a').on('click', function () {
                    var sort = $(this).data('sort');
                    if(sort === cur_sort) return;

                    if(sort === 'follow' && false){
                        window.location.href = '//www.douban.com/accounts/login?source=movie';
                        return;
                    }

                    if($('#reviews-wrapper .review_filter').data('doing')) return;
                    $('#reviews-wrapper .review_filter').data('doing', true);

                    cur_sort = sort;

                    $('#reviews-wrapper .review_filter a').removeClass('cur');
                    $(this).addClass('cur');

                    $.getJSON('reviews', { sort: sort }, function(res) {
                        $('#reviews-wrapper .review-list').remove();
                        $('#reviews-wrapper [href="reviews?sort=follow"]').parent().remove();
                        $('#reviews-wrapper .review_filter').after(res.html);
                        $('#reviews-wrapper .review_filter').data('doing', false);
                        $('#reviews-wrapper .review_filter').removeData('doing');

                        if (res.count === 0) {
                            $('#reviews-wrapper .review-list').html('<span class="no-review">你关注的人还没写过长评</span>');
                        }
                    });
                });
            </script>


            



<div class="review-list  ">
        
    

            
    
    <div data-cid="14542346">
        <div class="main review-item" id="14542346">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/mks20050729/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u191212696-7.jpg">
        </a>

        <a href="https://www.douban.com/people/mks20050729/" class="name">Nostalgia</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2022-07-29" class="main-meta">2022-07-29 10:38:09</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14542346/">《开心麻花》再无“开心”，只有“麻花”</a></h2>

                <div id="review_14542346_short" class="review-short" data-rid="14542346">
                    <div class="short-content">

                        整篇影评我从来没说这部电影是一个烂片，那些乱扣帽子的可以滚了，我的主页打的是三星，但是长评显示的是两分，不信去看我主页啊！ 有些团体真的搞笑 ，连我的观点看都不看直接开骂，我说出的我的真话可耻吗？我花了票钱难道不能表达观点吗？为什么要用你们强盗思维来堵住我的...

                        &nbsp;(<a href="javascript:;" id="toggle-14542346-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14542346_full" class="hidden">
                    <div id="review_14542346_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14542346" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14542346">
                                1614
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14542346" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14542346">
                                423
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14542346/#comments" class="reply cls_abnormal">1040回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14544321">
        <div class="main review-item" id="14544321">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/67745680/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u67745680-16.jpg">
        </a>

        <a href="https://www.douban.com/people/67745680/" class="name">北家</a>

            <span class="allstar10 main-title-rating" title="很差"></span>

        <span content="2022-07-30" class="main-meta">2022-07-30 01:48:05</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14544321/">个人年度最烂片，开心麻花你攒了个啥玩意儿！</a></h2>

                <div id="review_14544321_short" class="review-short" data-rid="14544321">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        激情开麦，这是我2021年3月至今，看过的院线+非院线电影里最烂的一部。 为什么时间算这么精准呢？因为去年春节档有个唐探三，我这个大冤种花了两张票价的钱去看了。 独行月球请谢谢唐探三，不然你可能成为我近五年看过的最烂的电影。 下面就要详细骂骂这部电影的烂了，影院里两...

                        &nbsp;(<a href="javascript:;" id="toggle-14544321-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14544321_full" class="hidden">
                    <div id="review_14544321_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14544321" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14544321">
                                1603
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14544321" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14544321">
                                440
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14544321/#comments" class="reply cls_abnormal">915回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14559762">
        <div class="main review-item" id="14559762">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/202844410/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u202844410-12.jpg">
        </a>

        <a href="https://www.douban.com/people/202844410/" class="name">方和斐</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2022-08-06" class="main-meta">2022-08-06 16:43:44</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14559762/">此片在天文方面的4个瑕疵和10个优点</a></h2>

                <div id="review_14559762_short" class="review-short" data-rid="14559762">
                    <div class="short-content">

                        国内的科幻特效确实已经做得不错，把天体现象复原得很好。不过还是要谈一下几个瑕疵： 1. 首先批评一个明显的问题：几个主演那么字正腔圆读出来的“长zhǎng存湖”，难道就没有查一下读音？人家叫做“长cháng存湖”！ （百度百科写的拼音也是错的，正确版本见天文学名词审定委...

                        &nbsp;(<a href="javascript:;" id="toggle-14559762-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14559762_full" class="hidden">
                    <div id="review_14559762_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14559762" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14559762">
                                523
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14559762" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14559762">
                                11
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14559762/#comments" class="reply cls_abnormal">131回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14542940">
        <div class="main review-item" id="14542940">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/firo/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u1799384-69.jpg">
        </a>

        <a href="https://www.douban.com/people/firo/" class="name">银谷</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2022-07-29" class="main-meta">2022-07-29 15:02:25</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14542940/">毫无疑问，这是沈腾最浪漫的一部电影。</a></h2>

                <div id="review_14542940_short" class="review-short" data-rid="14542940">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        冲着笑去的，结果却收获了意外的惊喜——极致的浪漫。 对，浪漫是我看完这部含腾量百分之百的《独行月球》电影后的第一感觉。 浪漫是——只是在电梯上那一眼万年，我就愿意为了靠近你从工程师变成维修工。 浪漫是——我总是在我们擦身而过的时候偷偷看你，可我不知道你也在回头...

                        &nbsp;(<a href="javascript:;" id="toggle-14542940-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14542940_full" class="hidden">
                    <div id="review_14542940_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14542940" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14542940">
                                1849
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14542940" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14542940">
                                180
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14542940/#comments" class="reply cls_abnormal">1122回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14544880">
        <div class="main review-item" id="14544880">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/gallimard/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u1196418-181.jpg">
        </a>

        <a href="https://www.douban.com/people/gallimard/" class="name">桃花石上书生</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2022-07-30" class="main-meta">2022-07-30 13:17:20</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14544880/">夸一夸沈腾那真诚的大脸和演技及其他</a></h2>

                <div id="review_14544880_short" class="review-short" data-rid="14544880">
                    <div class="short-content">

                        昨晚看了《独行月球》。不吹不黑，在近年来国内的科幻电影和喜剧电影两个类别里，这部电影都算是相当不错的。 第一个优势，是几个主角演技很不错。 好的喜剧演员，应该能够演出一个小人物的尴尬、悲伤，又演出小人物作为人的尊严高贵的一面，让你在他身上看到自己渺小而不屈的...

                        &nbsp;(<a href="javascript:;" id="toggle-14544880-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14544880_full" class="hidden">
                    <div id="review_14544880_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14544880" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14544880">
                                1373
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14544880" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14544880">
                                73
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14544880/#comments" class="reply cls_abnormal">827回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14542561">
        <div class="main review-item" id="14542561">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/175903445/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u175903445-1.jpg">
        </a>

        <a href="https://www.douban.com/people/175903445/" class="name">suitable</a>

            <span class="allstar20 main-title-rating" title="较差"></span>

        <span content="2022-07-29" class="main-meta">2022-07-29 11:48:54</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14542561/">实话实说的观影感受，没黑没喷，水J绕道</a></h2>

                <div id="review_14542561_short" class="review-short" data-rid="14542561">
                    <div class="short-content">

                        好消息是含腾量很高，坏消息是含腾量很高也不能作为无脑进影院的理由。 虽然我看完之后倒也没有后悔去看这个电影，但如果朋友问我值不值得推荐的话，我还是会迟疑的。 这部电影它确实不值得给别人推荐。《豆瓣开分7.3，一周左右降到6+，只能说DDDD》《客观评价两颗星，考虑到沈...

                        &nbsp;(<a href="javascript:;" id="toggle-14542561-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14542561_full" class="hidden">
                    <div id="review_14542561_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14542561" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14542561">
                                848
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14542561" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14542561">
                                293
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14542561/#comments" class="reply cls_abnormal">592回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14542497">
        <div class="main review-item" id="14542497">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/aowuuZXH/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u243176604-3.jpg">
        </a>

        <a href="https://www.douban.com/people/aowuuZXH/" class="name">12beansss</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2022-07-28" class="main-meta">2022-07-28 21:50:03</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14542497/">“宇宙这么大，我们还会遇见”</a></h2>

                <div id="review_14542497_short" class="review-short" data-rid="14542497">
                    <div class="short-content">

                        8.5/10分。瑕不掩瑜，我仍相信是一部能炸开疫/情之下沉闷已久的国内电影市场的好电影。 【无剧透环节】 优点1 含腾量很高，这部电影就像是为沈腾量身定做的大男主电影，不少飙车&amp;amp;操控航天器戏码让我觉得这个角色真的很帅~ 优点2 喜剧+科幻元素(非硬科幻)+煽情融合得很好，...

                        &nbsp;(<a href="javascript:;" id="toggle-14542497-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14542497_full" class="hidden">
                    <div id="review_14542497_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14542497" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14542497">
                                1228
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14542497" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14542497">
                                69
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14542497/#comments" class="reply cls_abnormal">779回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14545726">
        <div class="main review-item" id="14545726">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/EmeraldKinoko/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u4479476-6.jpg">
        </a>

        <a href="https://www.douban.com/people/EmeraldKinoko/" class="name">风蚀蘑菇</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2022-07-30" class="main-meta">2022-07-30 21:28:21</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14545726/">人人都说这是喜剧，我却为这孤绝的浪漫泪流满面</a></h2>

                <div id="review_14545726_short" class="review-short" data-rid="14545726">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        沈腾+马丽+开心麻花，似乎等号的另一边不假思索一定是喜剧。《独行月球》的前半部分确实也让我忍俊不禁，从独孤月完美错过撤离的平行剪辑，到目睹地球毁灭后的月球电子灵堂，到妖娆背影一转头却是厌世脸袋鼠“金刚鼠”，那句面容扭曲的“今天也是元气满满的一天啊啊啊——”让...

                        &nbsp;(<a href="javascript:;" id="toggle-14545726-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14545726_full" class="hidden">
                    <div id="review_14545726_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14545726" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14545726">
                                483
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14545726" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14545726">
                                12
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14545726/#comments" class="reply cls_abnormal">168回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14543011">
        <div class="main review-item" id="14543011">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/darkwood/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1218430-450.jpg">
        </a>

        <a href="https://www.douban.com/people/darkwood/" class="name">巴伐利亞酒神</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2022-07-29" class="main-meta">2022-07-29 15:30:37</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14543011/">独行月球：没有人比我们更接近对方</a></h2>

                <div id="review_14543011_short" class="review-short" data-rid="14543011">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        当《独行月球》行将结尾时，我在黑漆漆的放映厅里想起了一句歌词： “黑暗中 我们紧紧的相拥 看星空闪烁 就这样并排躺在一望无际 星河的中央 直到没有人能够比我们更为接近对方” 这是声音玩具的一首歌。此时此刻，它就像一首专为独孤月和马蓝星而谱写的情歌。在我看来，它甚至...

                        &nbsp;(<a href="javascript:;" id="toggle-14543011-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14543011_full" class="hidden">
                    <div id="review_14543011_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14543011" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14543011">
                                1036
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14543011" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14543011">
                                61
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14543011/#comments" class="reply cls_abnormal">726回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="14580330">
        <div class="main review-item" id="14580330">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/mxf1978/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u4206880-6.jpg">
        </a>

        <a href="https://www.douban.com/people/mxf1978/" class="name">梅雪风</a>


        <span content="2022-08-15" class="main-meta">2022-08-15 17:05:59</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/14580330/">《独行月球》：开心麻花式喜剧为什么越来越尴尬？</a></h2>

                <div id="review_14580330_short" class="review-short" data-rid="14580330">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        文｜梅雪风 一 它看起来像很多电影杂糅。它自我拯救的部分像《火星救援》，里面的人物设置及前面部分像《荒岛余生》，那只袋鼠其实是《荒岛余生》里那个叫威尔森的排球的升级版，而马丽那个角色，则是海伦·亨特那个角色的重生。至于影片中的喜剧成分，则是开心麻花喜剧手法零...

                        &nbsp;(<a href="javascript:;" id="toggle-14580330-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_14580330_full" class="hidden">
                    <div id="review_14580330_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="14580330" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-14580330">
                                84
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="14580330" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-14580330">
                                14
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/14580330/#comments" class="reply cls_abnormal">17回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>




    

    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/17dfbca9ee00936a.js"></script>
    <!-- COLLECTED CSS -->
</div>








                <p class="pl">
                    &gt;
                        <a href="reviews">
                            更多影评
                                3420篇
                        </a>
                </p>
    </section>
<!-- COLLECTED JS -->




    <br/>

    
            <div class="section-discussion">
                    
                    <div class="mod-hd">
                            <a class="comment_btn cls_abnormal" href="/subject/35183042/discussion/create" rel="nofollow"><span>添加新讨论</span></a>
                        
    <h2>
        讨论区
         &nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;
    </h2>

                    </div>
                    
  <table class="olt"><tr><td><td><td><td></tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/35183042/discussion/637327045/" title="地球上手电筒的光真的能穿越宇宙被月球看到？">地球上手电筒的光真的能穿越宇宙被月球看到？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/4148386/">mоmо</a></td>
          <td class="pl"><span>32 回应</span></td>
          <td class="pl"><span>2022-11-08 09:57:49</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/35183042/discussion/637333280/" title="此片买了《火星救援》的版权了吗？">此片买了《火星救援》的版权了吗？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/66254300/">灰机中的战斗机</a></td>
          <td class="pl"><span>4 回应</span></td>
          <td class="pl"><span>2022-11-08 08:36:13</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/35183042/discussion/637337626/" title="刚刚及格">刚刚及格</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/191336229/">三月鸟</a></td>
          <td class="pl"><span></span></td>
          <td class="pl"><span>2022-11-08 08:27:12</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/35183042/discussion/637270551/" title="说好看的都是小镇青年?">说好看的都是小镇青年?</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/191652656/">啦啦啦</a></td>
          <td class="pl"><span>91 回应</span></td>
          <td class="pl"><span>2022-11-08 02:52:08</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/35183042/discussion/637337592/" title="装B的很难满足，这片难道不比流浪地球好上很多">装B的很难满足，这片难道不比流浪地球好上很多</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/155094421/">人间腊月天</a></td>
          <td class="pl"><span></span></td>
          <td class="pl"><span>2022-11-08 02:51:05</span></td>
        </tr>
  </table>

                    <p class="pl" align="right">
                        <a href="/subject/35183042/discussion/" rel="nofollow">
                            &gt; 去这部影片的讨论区（全部2082条）
                        </a>
                    </p>
            </div>


    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside">
                


    








        






    

<script id="episode-tmpl" type="text/x-jsrender">
<div id="tv-play-source" class="play-source">
    <div class="cross">
        <span style="color:#494949; font-size:16px">{{:cn}}</span>
        <span style="cursor:pointer">✕</span>
    </div>
    <div class="episode-list">
        {{for playlist}}
            <a href="{{:play_link}}&episode={{:ep}}" target="_blank">{{:ep}}集</a>
        {{/for}}
     <div>
 </div>
</script>

<div class="gray_ad">
    
    <h2>
        在哪儿看这部电影
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

        <a href="/subject/35183042/report_subject_error?pname=在线观看" target="_blank" rel="nofollow" class="report-error">报错</a>
    
    <ul class="bs">
                
                <li>
                        <a class="playBtn" data-cn="咪咕视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=35183042&amp;video_type=movie&amp;video_id=922075&amp;source=miguvideo&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=35183042&amp;video_type=movie&amp;video_id=922075&amp;source=miguvideo&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3Fcid%3D747535355%26pwId%3Dd01197d3076b4164af82983c408bb996&amp;subtype=15&amp;type=online-video&amp;link2key=42fb1da4a8" target="_blank">
                            咪咕视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="芒果TV" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=35183042&amp;video_type=movie&amp;video_id=922086&amp;source=mgtv&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=35183042&amp;video_type=movie&amp;video_id=922086&amp;source=mgtv&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.mgtv.com%2Fb%2F420004%2F17593850.html%3Fcxid%3Dvb4rv4jhk&amp;subtype=7&amp;type=online-video" target="_blank">
                            芒果TV
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="优酷视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=35183042&amp;video_type=movie&amp;video_id=922048&amp;source=youku&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=35183042&amp;video_type=movie&amp;video_id=922048&amp;source=youku&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fv.youku.com%2Fv_show%2Fid_XNTkwNjQxMzE2NA%3D%3D.html%3Ftpa%3DdW5pb25faWQ9MzAwMDA4XzEwMDAwMl8wMl8wMQ%26refer%3Desfhz_operation.xuka.xj_00003036_000000_FNZfau_19010900&amp;subtype=3&amp;type=online-video" target="_blank">
                            优酷视频
                        </a>
                    <span class="buylink-price"><span>
                        单片付费
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="腾讯视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=35183042&amp;video_type=movie&amp;video_id=920110&amp;source=qq&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=35183042&amp;video_type=movie&amp;video_id=920110&amp;source=qq&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc002000y0q8uy.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video" target="_blank">
                            腾讯视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="爱奇艺视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=35183042&amp;video_type=movie&amp;video_id=922049&amp;source=iqiyi&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=35183042&amp;video_type=movie&amp;video_id=922049&amp;source=iqiyi&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_1e54n0pt5ro.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video" target="_blank">
                            爱奇艺视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>

    </ul>
</div>


    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right"></div>
    <div id="dale_movie_subject_top_middle"></div>
    <!-- douban ad end -->

    



<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>



    







<!--tags-->

    <div id="dale_subject_right_guess_you_like"></div>
    <div id="dale_movie_subject_inner_middle"></div>
    <div id="dale_movie_subject_download_middle"></div>
    
        








<div id="subject-doulist">
    
    
    <h2>
        <i class="">以下片单推荐</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/35183042/doulists">全部</a>
            )
            </span>
    </h2>


    
    <ul>
            
                <li>
                    <a href="https://www.douban.com/doulist/30299/" target="_blank">豆瓣电影【口碑榜】2022-06-13 更新</a>
                    <span>(影志)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/13712178/" target="_blank">评价人数超过十万的电影</a>
                    <span>(依然饭特稀)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/36298/" target="_blank">【影】笑炸了肺</a>
                    <span>(小米=qdmimi)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/43556971/" target="_blank">始终会看的电影</a>
                    <span>(可可)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/1434921/" target="_blank">2022—2024值得关注的华语电影</a>
                    <span>(closer)</span>
                </li>
    </ul>

</div>

    
        









<div id="subject-others-interests">
    
    
    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>

    
    <ul class="">
            
            <li class="">
                <a href="https://www.douban.com/people/54315867/" class="others-interest-avatar">
                    <img src="https://img9.doubanio.com/icon/u54315867-4.jpg" class="pil" alt="嗨呀">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/54315867/" class="">嗨呀</a>
                    <div class="">
                        刚刚
                        看过
                        <span class="allstar40" title="推荐"></span>
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/128621124/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u128621124-1.jpg" class="pil" alt="Cudoup">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/128621124/" class="">Cudoup</a>
                    <div class="">
                        3分钟前
                        看过
                        <span class="allstar20" title="较差"></span>
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/239827589/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u239827589-1.jpg" class="pil" alt="锖青磁">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/239827589/" class="">锖青磁</a>
                    <div class="">
                        4分钟前
                        看过
                        <span class="allstar20" title="较差"></span>
                    </div>
                </div>
            </li>
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/35183042/comments?status=P">616453人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/35183042/comments?status=F">45882人想看</a>
    </div>

</div>



    

<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br/>

    
<p class="pl">订阅独行月球的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/35183042/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">
                
    
<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->

    <!-- douban ad begin -->
    <div id="dale_movie_subject_hovering_video"></div>
    <!-- douban ad end -->

            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    &copy; 2005－2022 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/4773b4b00c451a2c.js"></script><script type="text/javascript">
        if (!Do.ready) {
            !function(){var t,e,n=document,r=window,i=window.__external_files_loaded=window.__external_files_loaded||{},o=window.__external_files_loading=window.__external_files_loading||{},a=function(t){return t.constructor===Array},s={autoLoad:!0,coreLib:["//img3.doubanio.com/js/jquery.min.js"],mods:{}},c=n.getElementsByTagName("script"),d=c[c.length-1],u=[],l=!1,f=[],h=function(t,e,r,a,s){var d=c[0];if(t){if(i[t])return o[t]=!1,void(a&&a(t,s));if(o[t])return void setTimeout(function(){h(t,e,r,a,s)},1);o[t]=!0;var u,l=e||t.toLowerCase().split(/\./).pop().replace(/[\?#].*/,"");if("js"===l?(u=n.createElement("script"),u.setAttribute("type","text/javascript"),u.setAttribute("src",t),u.setAttribute("async",!0)):"css"===l&&(u=n.createElement("link"),u.setAttribute("type","text/css"),u.setAttribute("rel","stylesheet"),u.setAttribute("href",t),i[t]=!0),u){if(r&&(u.charset=r),"css"===l)return d.parentNode.insertBefore(u,d),void(a&&a(t,s));u.onload=u.onreadystatechange=function(){this.readyState&&"loaded"!==this.readyState&&"complete"!==this.readyState||(i[this.getAttribute("src")]=!0,a&&a(this.getAttribute("src"),s),u.onload=u.onreadystatechange=null)},d.parentNode.insertBefore(u,d)}}},p=function(t){if(t&&a(t)){for(var e,n=0,r=[],i=s.mods,o=[],c={},d=function(t){var e,n,r=0;if(c[t])return o;if(c[t]=!0,i[t].requires){for(n=i[t].requires;"undefined"!=typeof(e=n[r++]);)i[e]?(d(e),o.push(e)):o.push(e);return o}return o};"undefined"!=typeof(e=t[n++]);)i[e]&&i[e].requires&&i[e].requires[0]&&(o=[],c={},r=r.concat(d(e))),r.push(e);return r}},y=function(){l=!0,u.length>0&&(e.apply(this,u),u=[])},m=function(){n.addEventListener?n.removeEventListener("DOMContentLoaded",m,!1):n.attachEvent&&n.detachEvent("onreadystatechange",m),y()},v=function(){if(!l){try{n.documentElement.doScroll("left")}catch(t){return r.setTimeout(v,1)}y()}},g=function(){if("complete"===n.readyState)return r.setTimeout(y,1);var t=!1;if(n.addEventListener)n.addEventListener("DOMContentLoaded",m,!1),r.addEventListener("load",y,!1);else if(n.attachEvent){n.attachEvent("onreadystatechange",m),r.attachEvent("onload",y);try{t=null===r.frameElement}catch(t){}document.documentElement.doScroll&&t&&v()}},E=function(t){t&&a(t)&&(this.queue=t,this.current=null)};E.prototype={_interval:10,start:function(){return this.current=this.next(),this.current?void this.run():void(this.end=!0)},run:function(){var t,e=this,n=this.current;return"function"==typeof n?(n(),void this.start()):void("string"==typeof n&&(s.mods[n]?(t=s.mods[n],h(t.path,t.type,t.charset,function(t){e.start()},e)):/\.js|\.css/i.test(n)?h(n,"","",function(t,e){e.start()},e):this.start()))},next:function(){return this.queue.shift()}},t=d.getAttribute("data-cfg-autoload"),"string"==typeof t&&(s.autoLoad="true"===t.toLowerCase()),t=d.getAttribute("data-cfg-corelib"),"string"==typeof t&&(s.coreLib=t.split(",")),e=function(){var t,e=[].slice.call(arguments);f.length>0&&(e=f.concat(e)),s.autoLoad&&(e=s.coreLib.concat(e)),t=new E(p(e)),t.start()},e.add=function(t,e){t&&e&&e.path&&(s.mods[t]=e)},e.delay=function(){var t=[].slice.call(arguments),n=t.shift();r.setTimeout(function(){e.apply(this,t)},n)},e.global=function(){var t=[].slice.call(arguments);f=f.concat(t)},e.ready=function(){var t=[].slice.call(arguments);return l?e.apply(this,t):void(u=u.concat(t))},e.css=function(t){var e=n.getElementById("do-inline-css");e||(e=n.createElement("style"),e.type="text/css",e.id="do-inline-css",n.getElementsByTagName("head")[0].appendChild(e)),e.styleSheet?e.styleSheet.cssText=e.styleSheet.cssText+t:e.appendChild(n.createTextNode(t))},s.autoLoad&&e(s.coreLib),e.define=e.add,e._config=s,e._mods=s.mods,this.Do=e,g()}();
        }
        function reportTrack(url) {
          if (!url) { return false }
          $.ajax({ url: url, dataType: 'text/html' })
        }
        Do.ready(
            'https://img3.doubanio.com/f/movie/b2a06a0332fc1526f4caaf8c76c2717d24da408d/js/movie/lib/jsrender.min.js',
            function(){
                $(document).on('click', '.cross span', function(e) {
                    var $this = $(this);
                    var $dialog = $this.parents('#tv-play-source');
                    $dialog.remove();
                });
                $('body').bind('click', function(e) {
                    var $this = $(e.target),
                        $source = $('.play-source');
                    if (!$this.is('.playBtn') && !$this.parents('.play-source').length) {
                        $source.remove();
                    }
                });
                var sources = {};
                sources[15] = [
                            {play_link: "https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3Fcid%3D747535355%26pwId%3Dd01197d3076b4164af82983c408bb996&amp;subtype=15&amp;type=online-video&amp;link2key=42fb1da4a8", ep: "1"},
                ];
                sources[7] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fwww.mgtv.com%2Fb%2F420004%2F17593850.html%3Fcxid%3Dvb4rv4jhk&amp;subtype=7&amp;type=online-video", ep: "1"},
                ];
                sources[3] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fv.youku.com%2Fv_show%2Fid_XNTkwNjQxMzE2NA%3D%3D.html%3Ftpa%3DdW5pb25faWQ9MzAwMDA4XzEwMDAwMl8wMl8wMQ%26refer%3Desfhz_operation.xuka.xj_00003036_000000_FNZfau_19010900&amp;subtype=3&amp;type=online-video", ep: "1"},
                ];
                sources[1] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc002000y0q8uy.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video", ep: "1"},
                ];
                sources[9] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_1e54n0pt5ro.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video", ep: "1"},
                ];
                $('.playBtn').each(function(i, item) {
                    // 曝光监测上报
                    if (item) {
                        reportTrack(item.dataset.impressionTrack);
                    }
                });
                $('.playBtn').click(function(e){
                    // 点击监测上报
                    reportTrack(e.target.dataset.clickTrack);
                    
                    $('.play-source').remove();

                    var height, width, tmpl, cn, source;
                    var $dialog = $('#tv-play-source');
                    var $this = $(this);
                    source = $this.data('source');
                    if(!source)return;
                    cn = $this.data('cn');

                    tmpl = $.templates('#episode-tmpl');
                    $dialog = $(tmpl.render({playlist: sources[source], cn: cn}));

                    $dialog.hide();
                    $('body').append($dialog);
                    width = $dialog.outerWidth();

                    $dialog.css({
                        marginLeft: -width / 2,
                        top: $this.offset().top + $this.outerHeight()
                    }).show();
                });
            });
    </script><script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/bfe0dd99ab8a2cf.js"></script>
    
        <script>
            window._USER_ABNORMAL = {"abnormal":{"status":"S"}}
        </script>
        <script type="text/javascript" src="https://img3.doubanio.com/f/shire/eedd954dfd0fb8d611a30cc1ecafeda9cccfe764/js/abnormal_account.js"></script>
    
    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '264064658',
            browserId = 'DcI5Fbd5RAQ',
            criteria = '7:沈腾|7:李诚儒|7:李海银|7:搞笑|7:黄才伦|7:中国大陆|7:李嘉琦|7:黄子韬|7:张吃鱼|7:开心麻花|7:马丽|7:杨皓宇|7:高海宝|7:杜晓宇|7:常远|7:张熙然|7:史彭元|7:徐志胜|7:郝瀚|7:陶亮|7:王成思|7:科幻|7:杨铮|7:王赞|7:电影|7:中国|7:黄品沅|7:2022|7:喜剧|3:/subject/35183042/',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle', 'dale_movie_subject_banner_after_intro', 'dale_subject_right_guess_you_like', 'dale_movie_subject_hovering_video'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/MnJwNGlleS9mL2FkanMvY2M1OGQyNTQ2N2I2YmQzOTlmNTliMGJiMjI4MWRhZTlkNTNjYTFkZC9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>











    
  









<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '1', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








      

    <!-- dae-web-movie--default-6b96d487b6-gwg6c-->

  <script>_SPLITTEST=''</script>
</body>

</html>
"""
douban_html = """

<!DOCTYPE html>
<html lang="zh-CN" class="ua-windows ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        大独裁者 (豆瓣)
</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/204847ecc7d679de915c283531d14f16cfbee65e/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/0b4cdb02dd620693709d9314196b617f17c2f9ea/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/252bef058b97005c6a41e8f1b9f7b06b84bc71b3/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/4888ee2fda6812f70a064a51c93b84fde8e4a3c2/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/b0d3faaf7a432605add54908e39e17746824d6cc/js/separation/_all.js"></script>
    
    <meta name="keywords" content="大独裁者,The Great Dictator,大独裁者影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="大独裁者电影简介和剧情介绍,大独裁者影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/movie/subject/1295646/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/1295646/" />
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/2c0c1c6b83f9a457b0f38c38a32fc43a42ec9bad/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/bc881a837a728ab82aa01d653b1c180190bb5a5d/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>
    
  <script type='text/javascript'>
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>


    


<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "name": "大独裁者 The Great Dictator",
  "url": "/subject/1295646/",
  "image": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1960167314.webp",
  "director": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1002724/",
      "name": "查理·卓别林 Charles Chaplin"
    }
  ]
,
  "author": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1002724/",
      "name": "查理·卓别林 Charles Chaplin"
    }
  ]
,
  "actor": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1002724/",
      "name": "查理·卓别林 Charles Chaplin"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1019107/",
      "name": "宝莲·高黛 Paulette Goddard"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1041556/",
      "name": "杰克·奥克 Jack Oakie"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1098631/",
      "name": "雷金纳德·加德纳 Reginald Gardiner"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1314759/",
      "name": "邱岳峰 Yuefeng Qiu"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1028904/",
      "name": "卡特·德黑文 Carter DeHaven"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1093820/",
      "name": "比利·吉尔伯特 Billy Gilbert"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1094202/",
      "name": "格蕾斯·海尔 Grace Hayle"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1067393/",
      "name": "亨利·丹尼尔 Henry Daniell"
    }
  ]
,
  "datePublished": "1940-10-15",
  "genre": ["\u559c\u5267", "\u5267\u60c5", "\u6218\u4e89"],
  "duration": "PT2H5M",
  "description": "影片讲述第一次世界大战，托曼尼亚王国独裁者辛格尔（查理·卓别林饰）上台。他的大肆扩张导致战乱不断民不聊生。并且他大搞阴谋政策，煽动民众对犹太人的敌对与仇恨，让犹太人民陷入水深火热的灾难之中。被征入伍的...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "72821",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "9.2"
  }
}
</script>

    
    
    <meta property="og:title" content="大独裁者 The Great Dictator" />
    <meta property="og:description" content="影片讲述第一次世界大战，托曼尼亚王国独裁者辛格尔（查理·卓别林饰）上台。他的大肆扩张导致战乱不断民不聊生。并且他大搞阴谋政策，煽动民众对犹太人的敌对与仇恨，让犹太人民陷入水深火热的灾难之中。被征入伍的..." />
    <meta property="og:site_name" content="豆瓣" />
    <meta property="og:url" content="https://movie.douban.com/subject/1295646/" />
    <meta property="og:image" content="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1960167314.webp" />
    <meta property="og:type" content="video.movie" />
            <meta property="video:actor" content="查理·卓别林" />
            <meta property="video:actor" content="宝莲·高黛" />
            <meta property="video:actor" content="杰克·奥克" />
            <meta property="video:actor" content="雷金纳德·加德纳" />
            <meta property="video:actor" content="邱岳峰" />
            <meta property="video:actor" content="卡特·德黑文" />
            <meta property="video:actor" content="比利·吉尔伯特" />
            <meta property="video:actor" content="格蕾斯·海尔" />
            <meta property="video:actor" content="亨利·丹尼尔" />
            <meta property="video:director" content="查理·卓别林" />
        <meta property="video:duration" content="7500" />


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/4f3b0c2711c6fd0a.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/3e96b44/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <ul>
    <li>
    <a id="top-nav-doumail-link" href="https://www.douban.com/doumail/">豆邮</a>
    </li>
    <li class="nav-user-account">
      <a target="_blank" href="https://accounts.douban.com/passport/setting/" class="bn-more">
        <span>AliceEngineer的帐号</span><span class="arrow"></span>
      </a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://www.douban.com/mine/">个人主页</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/orders/">我的订单</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/wallet/">我的钱包</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://accounts.douban.com/passport/setting/">帐号管理</a>
              </td>
            </tr>
            <tr>
              <td>
                <a href="https://www.douban.com/accounts/logout?source=movie&ck=F6Lh">退出</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  <div class="top-nav-reminder">
    <a href="https://www.douban.com/notification/" class="lnk-remind">提醒</a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
        <p>加载中...</p>
      </div>
    </div>
  </div>

    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;264064658&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;264064658&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;264064658&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;264064658&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;264064658&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;264064658&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;264064658&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;264064658&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;264064658&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;264064658&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    USER_ID: "264064658",
    UPLOAD_AUTH_TOKEN: "264064658:caa26b00fdbc4f55c0cb37f0f627f2127c8822d5",
    SSE_TOKEN: "f6671aa50280517e0d5cf305d5c50baaf6858069",
    SSE_TIMESTAMP: "1667929096",
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/3e96b44/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/3e96b44/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;search.douban.com&#47;movie/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/mine"
     >我看</a>
    </li>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual/2021?source=navigation"
     >2021年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2021?fullscreen=true&hidenav=true&autorotate=false&source=movie_navigation"
            target="_blank"
     >2021书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2021?source=movie_navigation" class="movieannual"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/3e96b44/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">大独裁者 The Great Dictator</span>
            <span class="year">(1940)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">
                    
                    


<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1002724/" rel="v:directedBy">查理·卓别林</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1002724/">查理·卓别林</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1002724/" rel="v:starring">查理·卓别林</a> / <a href="/celebrity/1019107/" rel="v:starring">宝莲·高黛</a> / <a href="/celebrity/1041556/" rel="v:starring">杰克·奥克</a> / <a href="/celebrity/1098631/" rel="v:starring">雷金纳德·加德纳</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">喜剧</span> / <span property="v:genre">战争</span><br/>
        
        <span class="pl">制片国家/地区:</span> 美国<br/>
        <span class="pl">语言:</span> 英语 / 世界语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="1940-10-15">1940-10-15</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="125">125 分钟</span><br/>
        <span class="pl">又名:</span> The Dictator / El gran dictador<br/>
        <span class="pl">IMDb:</span> tt0032553<br>

</div>




                </div>
                
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
            <div class="rating_logo ll">
                豆瓣评分
            </div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">9.2</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar45"></div>
        <div class="rating_sum">
                <a href="comments" class="rating_people">
                    <span property="v:votes">72821</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">65.4%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:28px"></div>
        <span class="rating_per">29.0%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:5px"></div>
        <span class="rating_per">5.2%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:0px"></div>
        <span class="rating_per">0.4%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:0px"></div>
        <span class="rating_per">0.1%</span>
        <br />
        </div>
</div>

    </div>
        
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=喜剧&type=24&interval_id=100:90&action=">99% 喜剧片</a><br/>
            好于 <a href="/typerank?type_name=战争&type=22&interval_id=100:90&action=">98% 战争片</a><br/>
        </div>
</div>


                
            </div>
            
                





<div id="interest_sect_level" class="clearfix">
        
            <a href="https://movie.douban.com/subject/1295646/?interest=wish&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-1295646-wish">
                <span>想看</span>
            </a>
            <a href="https://movie.douban.com/subject/1295646/?interest=collect&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-1295646-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1295646-collect-1">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1295646-collect-2">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1295646-collect-3">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1295646-collect-4">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1295646-collect-5">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/>
        </a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>
    

</div>


            

















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                
                  <li> 
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt'})" href="javascript:;" class="j a_collect_btn" name="cbtn-1295646">写短评</a>
 </li>
                  <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv'})" class="cls_abnormal" href="https://movie.douban.com/subject/1295646/new_review" rel="nofollow">写影评</a>
 </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
        });
    </script>
</div>




            

            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_1295646"></div>


        



<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">大独裁者的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report-intra">
                    
                        <span property="v:summary" class="">
                                　　影片讲述第一次世界大战，托曼尼亚王国独裁者辛格尔（查理·卓别林饰）上台。他的大肆扩张导致战乱不断民不聊生。并且他大搞阴谋政策，煽动民众对犹太人的敌对与仇恨，让犹太人民陷入水深火热的灾难之中。被征入伍的犹太人理发师查理（查理·卓别林饰）更是在这样的高压政策下难逃一劫。当查理逃出边境时，被驻守在这里的军队误认为是独裁者辛格尔，他趁机做了一场“为自由而战斗”的大演说。
                                    <br />
                                　　该片是查理·卓别林的第一部有声片，摄于希特勒统治最为黑暗的时期，片中对他辛辣讽刺跟丑化比比皆是。本片荣获第13届（1941）奥斯卡最佳电影、最佳男主角、最佳男配角、最佳编剧、最佳音乐5项提名。
                        </span>
                        <span class="pl"><a href="https://movie.douban.com/help/movie#t0-qs">&copy;豆瓣</a></span>
            </div>
</div>


    <div id="dale_movie_subject_banner_after_intro"></div>

    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">大独裁者的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/1295646/celebrities">全部 10</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1002724/" title="查理·卓别林 Charles Chaplin" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p1374279154.42.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1002724/" title="查理·卓别林 Charles Chaplin" class="name">查理·卓别林</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1002724/" title="查理·卓别林 Charles Chaplin" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p1374279154.42.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1002724/" title="查理·卓别林 Charles Chaplin" class="name">查理·卓别林</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1019107/" title="宝莲·高黛 Paulette Goddard" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p1388727761.93.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1019107/" title="宝莲·高黛 Paulette Goddard" class="name">宝莲·高黛</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1041556/" title="杰克·奥克 Jack Oakie" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p14473.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1041556/" title="杰克·奥克 Jack Oakie" class="name">杰克·奥克</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1098631/" title="雷金纳德·加德纳 Reginald Gardiner" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/raw/public/p1507471088.0.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1098631/" title="雷金纳德·加德纳 Reginald Gardiner" class="name">雷金纳德·加德纳</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1314759/" title="邱岳峰 Yuefeng Qiu" class="">
      <div class="avatar" style="background-image: url(https://img9.doubanio.com/view/celebrity/raw/public/p1609351576.95.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1314759/" title="邱岳峰 Yuefeng Qiu" class="name">邱岳峰</a></span>

      <span class="role" title="配音">配音</span>

    </div>
  </li>


  </ul>
</div>


    


<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/fada435abd10ae2583d995730a9e06e6e20a9a05/entry_creator/dist/author_subject/style.css">
<div id="author_subject" class="author-wrapper">
    <div class="loading"></div>
</div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '1295646',
      USER_ID: '264064658'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/82d2333c56fe1813ad6ee312f35a915941d906ae/entry_creator/dist/author_subject/index.js"></script>


    

    

    



<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>


<div class="mod">
    <div class="hd">
        
    <h2>
        <i class="">大独裁者的获奖情况</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1295646/awards/">全部</a>
            )
            </span>
    </h2>

    </div>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/Oscar/13/">第13届奥斯卡金像奖</a>
            </li>
            <li>最佳影片(提名)</li>
            <li></li>
        </ul>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/Oscar/13/">第13届奥斯卡金像奖</a>
            </li>
            <li>最佳男主角(提名)</li>
            <li><a href='https://movie.douban.com/celebrity/1002724/' target='_blank'>查理·卓别林</a></li>
        </ul>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/Oscar/13/">第13届奥斯卡金像奖</a>
            </li>
            <li>最佳男配角(提名)</li>
            <li><a href='https://movie.douban.com/celebrity/1041556/' target='_blank'>杰克·奥克</a></li>
        </ul>
</div>


    
        








    <div id="recommendations" class="">
        
        
    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>

        
    
    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1298817/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1581774481.webp" alt="淘金记" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1298817/?from=subject-page" class="" >淘金记</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1293270/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2506524685.webp" alt="寻子遇仙记" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1293270/?from=subject-page" class="" >寻子遇仙记</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1299628/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1959764913.webp" alt="马戏团" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1299628/?from=subject-page" class="" >马戏团</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1293908/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2170238828.webp" alt="城市之光" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1293908/?from=subject-page" class="" >城市之光</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1294371/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2263408369.webp" alt="摩登时代" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1294371/?from=subject-page" class="" >摩登时代</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292897/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p905332012.webp" alt="从军记" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292897/?from=subject-page" class="" >从军记</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1296909/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2399597512.webp" alt="虎口脱险" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1296909/?from=subject-page" class="" >虎口脱险</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1303408/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2206737207.webp" alt="福尔摩斯二世" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1303408/?from=subject-page" class="" >福尔摩斯二世</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292778/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2248676081.webp" alt="将军号" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292778/?from=subject-page" class="" >将军号</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292574/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p860250155.webp" alt="热情如火" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292574/?from=subject-page" class="" >热情如火</a>
            </dd>
        </dl>
    </div>

    </div>



    
        



<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}vote-comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content_tmpl content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>












    

    <div id="comments-section">
        <div class="mod-hd">
            
            
        <a class="comment_btn j a_collect_btn" name="cbtn-1295646" href="javascript:;" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">大独裁者的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1295646/comments?status=P">全部 15667 条</a>
            )
            </span>
    </h2>

        </div>
       
        


        <div class="mod-bd">
                
        <div class="tab-hd">
                        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
                        <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
                        <a id="following-comments-tab" href="comments?sort=follows" data-id="following" >好友</a>
        </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    

        
        <div class="comment-item " data-cid="909654162">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">318</span>

                    <input value="909654162" type="hidden"/>
                    <a href="javascript:;" data-id="909654162"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/PandaMovieMusic/" class="">Panda的影音</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2015-04-05 11:04:49">
                    2015-04-05 11:04:49
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">搞笑的动作语言是属于默片时代的，激情昂扬的反独裁演讲是属于有声电影的，因为《卓别林》传中关于本片的点滴描述激发了完整观影的冲动，能在纳粹独裁最猖狂的时候，在法西斯的施压下，拍出如此作品，不得不佩服卓别林的勇气和正义之心。——“独裁者会死去，他们从人民手里夺去的权利即将归还人民”。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1295646/?comment_id=909654162"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="1068138820">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">252</span>

                    <input value="1068138820" type="hidden"/>
                    <a href="javascript:;" data-id="1068138820"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/jeffersontang/" class="">巴喆</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2016-07-31 12:50:16">
                    2016-07-31 12:50:16
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">“遗憾得很，我并不想当皇帝，那不是我干的行当。我既不想统治任何人，也不想征服任何人。如果可能的话，我倒挺想帮助所有的人，不论是犹太人还是非犹太人，是黑种人还是白种人。我们都要互相帮助。做人就是应当如此。我们要把生活建筑在别人的幸福上，而不是建筑在别人的痛苦上。我们不要彼此仇恨......”9</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1295646/?comment_id=1068138820"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="2868653808">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">178</span>

                    <input value="2868653808" type="hidden"/>
                    <a href="javascript:;" data-id="2868653808"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/219235425/" class="">γ</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2021-08-27 19:15:56">
                    2021-08-27 19:15:56
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">竟然有人觉得最后的演讲是败笔？
我觉得这是使影片的最妙的升华！
这演讲单独拿出来都是永不过时的经典！
艺术需要唤醒麻木！特别是当下！
不能一见到艺术和政治挂钩就反感，艺术可以和政治挂钩，为政治服务。
我们需要更多的这样的作品而不只是娱乐至死。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1295646/?comment_id=2868653808"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="4094906">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">330</span>

                    <input value="4094906" type="hidden"/>
                    <a href="javascript:;" data-id="4094906"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/1170905/" class="">幸福超市总经理</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2006-07-15 03:27:42">
                    2006-07-15 03:27:42
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">现在看仍然有意义</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1295646/?comment_id=4094906"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>
        
        <div class="comment-item " data-cid="738053619">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">180</span>

                    <input value="738053619" type="hidden"/>
                    <a href="javascript:;" data-id="738053619"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/putengfei/" class="">大-燕-威-王</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2013-10-23 01:20:02">
                    2013-10-23 01:20:02
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">笑疯了。怪不得卓别林说只要能让他知道希特勒对这片儿的观感，无论让他付出啥代价他都愿意。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1295646/?comment_id=738053619"></div>
    </div>
    <script>
        (function(){
            $("body").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
                switch (e.type) {
                    case "mouseenter":
                    $(this).find(".comment-report").css('visibility', 'visible');
                    break;
                    case "mouseleave":
                    $(this).find(".comment-report").css('visibility', 'hidden');
                    break;
                }
            });
        })()
    </script>

        </div>




                
                    &gt; <a href="comments?sort=new_score&status=P" >
                        更多短评
                            15667条
                    </a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    




        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>
    
  <link rel="stylesheet" href="https://img3.doubanio.com/f/vendors/7d8c54c10ffd51769880282d4a41609dc465b796/reports.css" />
  <style>
    .btn-report { float: right; color: #bbb; cursor: pointer; font-size: 13px; }
  </style>
  <script src="https://img3.doubanio.com/f/vendors/bd6325a12f40c34cbf2668aafafb4ccd60deab7e/vendors.js"></script>
  <script src="https://img3.doubanio.com/f/vendors/68e2c291c7d4971661f7e4c3e41e1e99e2c2df4b/reports.js"></script>
  <script>
    (function () {
      var ADD_REPORT = function() {
        var roots = document.querySelectorAll(".comment-report");
        roots.forEach(function (root) {
          var btn = document.createElement('span');
          btn.className = 'btn-report';
          btn.innerHTML = "投诉";
          btn.addEventListener('click', function () {
            if (window.DOUBAN_VENDORS && window.DOUBAN_VENDORS.openReportModal) {
              window.DOUBAN_VENDORS.openReportModal({
                reportUrl: "" || root.getAttribute('data-url'),
                types: ["content"]
              })
            }
          });
          root.appendChild(btn);
        })
      }
      ADD_REPORT();
      window.ADD_REPORT = ADD_REPORT;
    })()
  </script>



            
            
        </div>
    </div>



<!--        此处是挂载其他页面，不是注释！不是注释！不是注释！-->
        


<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/6078555e83c38f2.css">

    <section id="reviews-wrapper" class="reviews mod movie-content">
        <header>
            
                <a href="new_review" rel="nofollow" class="create-review comment_btn cls_abnormal"
                    data-isverify="True"
                    data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/1295646/new_review">
                    <span>我要写影评</span>
                </a>
            <h2>
                    大独裁者的影评 · · · · · ·

                    <span class="pl">( <a href="reviews">全部 184 条</a> )</span>
            </h2>
        </header>

            <div class="review_filter">
                            <a href="javascript:;;" class="cur" data-sort="">热门</a> &#047;
                            <a href="javascript:;;" data-sort="time">最新</a> &#047;
                            <a href="javascript:;;" data-sort="follow">好友</a>
            </div>
            <script>
                var cur_sort = '';
                $('#reviews-wrapper .review_filter a').on('click', function () {
                    var sort = $(this).data('sort');
                    if(sort === cur_sort) return;

                    if(sort === 'follow' && false){
                        window.location.href = '//www.douban.com/accounts/login?source=movie';
                        return;
                    }

                    if($('#reviews-wrapper .review_filter').data('doing')) return;
                    $('#reviews-wrapper .review_filter').data('doing', true);

                    cur_sort = sort;

                    $('#reviews-wrapper .review_filter a').removeClass('cur');
                    $(this).addClass('cur');

                    $.getJSON('reviews', { sort: sort }, function(res) {
                        $('#reviews-wrapper .review-list').remove();
                        $('#reviews-wrapper [href="reviews?sort=follow"]').parent().remove();
                        $('#reviews-wrapper .review_filter').after(res.html);
                        $('#reviews-wrapper .review_filter').data('doing', false);
                        $('#reviews-wrapper .review_filter').removeData('doing');

                        if (res.count === 0) {
                            $('#reviews-wrapper .review-list').html('<span class="no-review">你关注的人还没写过长评</span>');
                        }
                    });
                });
            </script>


            



<div class="review-list  ">
        
    

            
    
    <div data-cid="1603922">
        <div class="main review-item" id="1603922">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/pipicat/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u1076234-1.jpg">
        </a>

        <a href="https://www.douban.com/people/pipicat/" class="name">牧神之箫</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2009-01-01" class="main-meta">2009-01-01 11:23:16</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1603922/">Fight For Liberty 为自由而战斗</a></h2>

                <div id="review_1603922_short" class="review-short" data-rid="1603922">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        此片结尾的演说Fight For Liberty（为自由而战斗）是公认的卓别林一生中最精彩的演说。长达7分钟的演说更被Timo Tolkki选进其专辑&lt;&lt;Hymn To Life&gt;&gt;的同名歌曲&#34;Hymn To Life.&#34; 　　Fight For Liberty（The Final Speech of “the Great Dictator”） 　　为自由而战斗（《大独裁...

                        &nbsp;(<a href="javascript:;" id="toggle-1603922-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1603922_full" class="hidden">
                    <div id="review_1603922_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1603922" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1603922">
                                766
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1603922" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1603922">
                                17
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1603922/#comments" class="reply cls_abnormal">61回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="2863124">
        <div class="main review-item" id="2863124">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/22145932/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u22145932-6.jpg">
        </a>

        <a href="https://www.douban.com/people/22145932/" class="name">以恒</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2009-12-15" class="main-meta">2009-12-15 22:48:35</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/2863124/">大独裁者最后演讲台词</a></h2>

                <div id="review_2863124_short" class="review-short" data-rid="2863124">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        I&#39;m sorry but I don&#39;t want to be an Emperor - that&#39;s not my business - I don&#39;t want to rule or conquer anyone. I should like to help everyone if possible, Jew, gentile, black man, white. We all want to help one another, human beings are like that. We want t...

                        &nbsp;(<a href="javascript:;" id="toggle-2863124-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_2863124_full" class="hidden">
                    <div id="review_2863124_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="2863124" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-2863124">
                                469
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="2863124" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-2863124">
                                16
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/2863124/#comments" class="reply cls_abnormal">21回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="4978991">
        <div class="main review-item" id="4978991">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/1282175/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u1282175-1.jpg">
        </a>

        <a href="https://www.douban.com/people/1282175/" class="name">雪</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2011-06-06" class="main-meta">2011-06-06 19:34:39</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/4978991/">演讲辞</a></h2>

                <div id="review_4978991_short" class="review-short" data-rid="4978991">
                    <div class="short-content">

                        对不起，但我不想成为什么皇帝 I&#39;m sorry, but I don&#39;t want to be an emperor.  那不是我的事情 That&#39;s not my business.  我不想统治或征服任何人 I don&#39;t want to rule or conquer anyone.  我想帮助每个人: I should like to help everyone:  犹太人，非犹太人，黑人，白人...

                        &nbsp;(<a href="javascript:;" id="toggle-4978991-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_4978991_full" class="hidden">
                    <div id="review_4978991_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="4978991" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-4978991">
                                113
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="4978991" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-4978991">
                                6
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/4978991/#comments" class="reply cls_abnormal">8回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="1340370">
        <div class="main review-item" id="1340370">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/NeeDream/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u1699417-116.jpg">
        </a>

        <a href="https://www.douban.com/people/NeeDream/" class="name">N</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2008-03-31" class="main-meta">2008-03-31 09:57:43</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1340370/">错过卓别林</a></h2>

                <div id="review_1340370_short" class="review-short" data-rid="1340370">
                    <div class="short-content">

                        过去对于卓别林的认识仅限于那个滑稽的流浪汉，觉得他是个幽默的人道主义者，用微笑擦去穷人脸上的泪水。今天看了《大独裁者》，才明白，他是一个真正的理想主义者，一个缔造美好未来的艺术家，一个伟大的造梦者！  下面这一段是他在影片结尾的演说。 不管民主、自由是对是错，...

                        &nbsp;(<a href="javascript:;" id="toggle-1340370-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1340370_full" class="hidden">
                    <div id="review_1340370_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1340370" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1340370">
                                59
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1340370" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1340370">
                                3
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1340370/#comments" class="reply cls_abnormal">13回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="8680046">
        <div class="main review-item" id="8680046">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/148376167/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u148376167-13.jpg">
        </a>

        <a href="https://www.douban.com/people/148376167/" class="name">槑槑</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2017-07-19" class="main-meta">2017-07-19 22:53:49</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/8680046/">卓别林</a></h2>

                <div id="review_8680046_short" class="review-short" data-rid="8680046">
                    <div class="short-content">

                        其实不如卓别林默片巅峰时期的几部作品艺术成就高，但在纳粹最嚣张的时候拍这样一部电影还是需要勇气的。作为卓别林第一部有声电影，最后七分钟的演讲却已经是公认的卓别林演艺生涯中最好的演讲。 但是作为卓别林的第一部有声电影，其影响已超越了一部电影。但笑点与故事桥段或...

                        &nbsp;(<a href="javascript:;" id="toggle-8680046-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_8680046_full" class="hidden">
                    <div id="review_8680046_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="8680046" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-8680046">
                                44
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="8680046" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-8680046">
                                2
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/8680046/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="7112731">
        <div class="main review-item" id="7112731">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/xiaoxiaodeyuanz/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u14597285-56.jpg">
        </a>

        <a href="https://www.douban.com/people/xiaoxiaodeyuanz/" class="name">远子</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2014-09-27" class="main-meta">2014-09-27 20:49:58</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/7112731/">希特勒的胡子</a></h2>

                <div id="review_7112731_short" class="review-short" data-rid="7112731">
                    <div class="short-content">

                        看完电影后，我想弄明白希特勒的胡子是怎么回事，为什么跟卓别林的那么像？  网上有资料说，在第一次世界大战爆发前，希特勒式的板刷胡是一种上层社会的时尚，蓄者多为柏林和维也纳的花花公子，一位德国民间英雄令它成为大众追捧的对象。此人名叫Hans Koeppen，是普鲁士一名飞...

                        &nbsp;(<a href="javascript:;" id="toggle-7112731-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_7112731_full" class="hidden">
                    <div id="review_7112731_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="7112731" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-7112731">
                                63
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="7112731" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-7112731">
                                10
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/7112731/#comments" class="reply cls_abnormal">5回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="12445329">
        <div class="main review-item" id="12445329">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/maverick0806/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u4843227-43.jpg">
        </a>

        <a href="https://www.douban.com/people/maverick0806/" class="name">Maverick</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2020-03-28" class="main-meta">2020-03-28 09:39:36</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/12445329/">《大独裁者》电影剧本</a></h2>

                <div id="review_12445329_short" class="review-short" data-rid="12445329">
                    <div class="short-content">

                        《大独裁者》电影剧本 译/李正伦 字幕： 虽然独裁者兴格尔和犹太人理发师两人完全相像，那不过纯粹出于巧合而已。——这里叙述的是在两次世界大战之间，疯狂支配了某一时期的故事。这个时间，自由遭到践踏，人性被横加蹂躏。 1918年第一次世界大战 战场。 蜿蜒曲折的战壕里，士...

                        &nbsp;(<a href="javascript:;" id="toggle-12445329-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_12445329_full" class="hidden">
                    <div id="review_12445329_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="12445329" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-12445329">
                                28
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="12445329" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-12445329">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/12445329/#comments" class="reply cls_abnormal">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="3513065">
        <div class="main review-item" id="3513065">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/wanhuasheng/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u3113630-6.jpg">
        </a>

        <a href="https://www.douban.com/people/wanhuasheng/" class="name">喜乐多鸿</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2010-08-06" class="main-meta">2010-08-06 16:43:11</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/3513065/">人性之贱，贱在凤姐的风骚很值钱</a></h2>

                <div id="review_3513065_short" class="review-short" data-rid="3513065">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        卓别林，一生最精彩的演说，道出了人性永恒关切的本质。战争仅仅是这些内在的表象，而已。  影片中，无知残害的大独裁者和善良失忆的理发师是同一个角色，在大独裁者最后演讲的那一刻，阴差阳错，角色转换。不仅卓别林自己向往真的转变，而具良知的人都渴望：站在台上，留着一...

                        &nbsp;(<a href="javascript:;" id="toggle-3513065-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_3513065_full" class="hidden">
                    <div id="review_3513065_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="3513065" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-3513065">
                                39
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="3513065" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-3513065">
                                3
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/3513065/#comments" class="reply cls_abnormal">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="2640768">
        <div class="main review-item" id="2640768">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/2101763/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u2101763-19.jpg">
        </a>

        <a href="https://www.douban.com/people/2101763/" class="name">千年古都的宅女</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2009-10-28" class="main-meta">2009-10-28 18:15:28</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/2640768/">我来猜猜希特勒看过此片后在想什么</a></h2>

                <div id="review_2640768_short" class="review-short" data-rid="2640768">
                    <div class="short-content">

                              希特勒在想：个培林把我包装的那么好，难道这个世界上还有不害怕或者是崇拜我的人嘛？     听了很多纳粹的笑话，总觉得希特勒这个魔鬼头子也很可爱，尽管不了解他究竟是怎么样的人。不过想想成为魔鬼的条件，也不得不对这个小个子肃然起敬。     1.拥有和神差不多的能力...

                        &nbsp;(<a href="javascript:;" id="toggle-2640768-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_2640768_full" class="hidden">
                    <div id="review_2640768_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="2640768" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-2640768">
                                22
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="2640768" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-2640768">
                                5
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/2640768/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>




    

    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/17dfbca9ee00936a.js"></script>
    <!-- COLLECTED CSS -->
</div>








                <p class="pl">
                    &gt;
                        <a href="reviews">
                            更多影评
                                184篇
                        </a>
                </p>
    </section>
<!-- COLLECTED JS -->




    <br/>

    

        
    
        
                
            


    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside">
                


    








        






    

<script id="episode-tmpl" type="text/x-jsrender">
<div id="tv-play-source" class="play-source">
    <div class="cross">
        <span style="color:#494949; font-size:16px">{{:cn}}</span>
        <span style="cursor:pointer">✕</span>
    </div>
    <div class="episode-list">
        {{for playlist}}
            <a href="{{:play_link}}&episode={{:ep}}" target="_blank">{{:ep}}集</a>
        {{/for}}
     <div>
 </div>
</script>

<div class="gray_ad">
    
    <h2>
        在哪儿看这部电影
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

        <a href="/subject/1295646/report_subject_error?pname=在线观看" target="_blank" rel="nofollow" class="report-error">报错</a>
    
    <ul class="bs">
                
                <li>
                        <a class="playBtn" data-cn="咪咕视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1295646&amp;video_type=movie&amp;video_id=757950&amp;source=miguvideo&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1295646&amp;video_type=movie&amp;video_id=757950&amp;source=miguvideo&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3Fcid%3D677040723%26pwId%3Dd01197d3076b4164af82983c408bb996&amp;subtype=15&amp;type=online-video&amp;link2key=42fb1da4a8" target="_blank">
                            咪咕视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="腾讯视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1295646&amp;video_type=movie&amp;video_id=304881&amp;source=qq&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1295646&amp;video_type=movie&amp;video_id=304881&amp;source=qq&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F0iwg66rmn19yseb.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video" target="_blank">
                            腾讯视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="爱奇艺视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1295646&amp;video_type=movie&amp;video_id=792437&amp;source=iqiyi&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1295646&amp;video_type=movie&amp;video_id=792437&amp;source=iqiyi&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_19rrj6sk8k.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video" target="_blank">
                            爱奇艺视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="哔哩哔哩" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1295646&amp;video_type=movie&amp;video_id=671493&amp;source=bilibili&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1295646&amp;video_type=movie&amp;video_id=671493&amp;source=bilibili&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=https%3A%2F%2Fwww.bilibili.com%2Fbangumi%2Fplay%2Fss28424%3Fbsource%3Ddouban&amp;subtype=8&amp;type=online-video&amp;link2key=42fb1da4a8" target="_blank">
                            哔哩哔哩
                        </a>
                    <span class="buylink-price"><span>
                        免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="1905电影网" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1295646&amp;video_type=movie&amp;video_id=597567&amp;source=cctv6&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1295646&amp;video_type=movie&amp;video_id=597567&amp;source=cctv6&amp;user_id=264064658&amp;bid=DcI5Fbd5RAQ&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fvip.1905.com%2Fplay%2F1333716.shtml%3F__hz%3D6e0721b2c6977135%26api_source%3Ddouban_vodadd&amp;subtype=13&amp;type=online-video" target="_blank">
                            1905电影网
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>

    </ul>
</div>


    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right"></div>
    <div id="dale_movie_subject_top_middle"></div>
    <!-- douban ad end -->

    



<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>



    








    <div id="dale_subject_right_guess_you_like"></div>
    <div id="dale_movie_subject_inner_middle"></div>
    <div id="dale_movie_subject_download_middle"></div>
    
    
        









<div id="subject-others-interests">
    
    
    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>

    
    <ul class="">
            
            <li class="">
                <a href="https://www.douban.com/people/175412223/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u175412223-2.jpg" class="pil" alt="Ask">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/175412223/" class="">Ask</a>
                    <div class="">
                        5分钟前
                        看过
                        <span class="allstar40" title="推荐"></span>
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/255944752/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u255944752-1.jpg" class="pil" alt="归未">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/255944752/" class="">归未</a>
                    <div class="">
                        46分钟前
                        看过
                        
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/205346999/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u205346999-1.jpg" class="pil" alt="赵大海">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/205346999/" class="">赵大海</a>
                    <div class="">
                        58分钟前
                        看过
                        
                    </div>
                </div>
            </li>
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/1295646/comments?status=P">114844人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/1295646/comments?status=F">57000人想看</a>
    </div>

</div>



    

<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br/>

    
<p class="pl">订阅大独裁者的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/1295646/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">
                
    
<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->

    <!-- douban ad begin -->
    <div id="dale_movie_subject_hovering_video"></div>
    <!-- douban ad end -->

            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    &copy; 2005－2022 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/4773b4b00c451a2c.js"></script><script type="text/javascript">
        if (!Do.ready) {
            !function(){var t,e,n=document,r=window,i=window.__external_files_loaded=window.__external_files_loaded||{},o=window.__external_files_loading=window.__external_files_loading||{},a=function(t){return t.constructor===Array},s={autoLoad:!0,coreLib:["//img3.doubanio.com/js/jquery.min.js"],mods:{}},c=n.getElementsByTagName("script"),d=c[c.length-1],u=[],l=!1,f=[],h=function(t,e,r,a,s){var d=c[0];if(t){if(i[t])return o[t]=!1,void(a&&a(t,s));if(o[t])return void setTimeout(function(){h(t,e,r,a,s)},1);o[t]=!0;var u,l=e||t.toLowerCase().split(/\./).pop().replace(/[\?#].*/,"");if("js"===l?(u=n.createElement("script"),u.setAttribute("type","text/javascript"),u.setAttribute("src",t),u.setAttribute("async",!0)):"css"===l&&(u=n.createElement("link"),u.setAttribute("type","text/css"),u.setAttribute("rel","stylesheet"),u.setAttribute("href",t),i[t]=!0),u){if(r&&(u.charset=r),"css"===l)return d.parentNode.insertBefore(u,d),void(a&&a(t,s));u.onload=u.onreadystatechange=function(){this.readyState&&"loaded"!==this.readyState&&"complete"!==this.readyState||(i[this.getAttribute("src")]=!0,a&&a(this.getAttribute("src"),s),u.onload=u.onreadystatechange=null)},d.parentNode.insertBefore(u,d)}}},p=function(t){if(t&&a(t)){for(var e,n=0,r=[],i=s.mods,o=[],c={},d=function(t){var e,n,r=0;if(c[t])return o;if(c[t]=!0,i[t].requires){for(n=i[t].requires;"undefined"!=typeof(e=n[r++]);)i[e]?(d(e),o.push(e)):o.push(e);return o}return o};"undefined"!=typeof(e=t[n++]);)i[e]&&i[e].requires&&i[e].requires[0]&&(o=[],c={},r=r.concat(d(e))),r.push(e);return r}},y=function(){l=!0,u.length>0&&(e.apply(this,u),u=[])},m=function(){n.addEventListener?n.removeEventListener("DOMContentLoaded",m,!1):n.attachEvent&&n.detachEvent("onreadystatechange",m),y()},v=function(){if(!l){try{n.documentElement.doScroll("left")}catch(t){return r.setTimeout(v,1)}y()}},g=function(){if("complete"===n.readyState)return r.setTimeout(y,1);var t=!1;if(n.addEventListener)n.addEventListener("DOMContentLoaded",m,!1),r.addEventListener("load",y,!1);else if(n.attachEvent){n.attachEvent("onreadystatechange",m),r.attachEvent("onload",y);try{t=null===r.frameElement}catch(t){}document.documentElement.doScroll&&t&&v()}},E=function(t){t&&a(t)&&(this.queue=t,this.current=null)};E.prototype={_interval:10,start:function(){return this.current=this.next(),this.current?void this.run():void(this.end=!0)},run:function(){var t,e=this,n=this.current;return"function"==typeof n?(n(),void this.start()):void("string"==typeof n&&(s.mods[n]?(t=s.mods[n],h(t.path,t.type,t.charset,function(t){e.start()},e)):/\.js|\.css/i.test(n)?h(n,"","",function(t,e){e.start()},e):this.start()))},next:function(){return this.queue.shift()}},t=d.getAttribute("data-cfg-autoload"),"string"==typeof t&&(s.autoLoad="true"===t.toLowerCase()),t=d.getAttribute("data-cfg-corelib"),"string"==typeof t&&(s.coreLib=t.split(",")),e=function(){var t,e=[].slice.call(arguments);f.length>0&&(e=f.concat(e)),s.autoLoad&&(e=s.coreLib.concat(e)),t=new E(p(e)),t.start()},e.add=function(t,e){t&&e&&e.path&&(s.mods[t]=e)},e.delay=function(){var t=[].slice.call(arguments),n=t.shift();r.setTimeout(function(){e.apply(this,t)},n)},e.global=function(){var t=[].slice.call(arguments);f=f.concat(t)},e.ready=function(){var t=[].slice.call(arguments);return l?e.apply(this,t):void(u=u.concat(t))},e.css=function(t){var e=n.getElementById("do-inline-css");e||(e=n.createElement("style"),e.type="text/css",e.id="do-inline-css",n.getElementsByTagName("head")[0].appendChild(e)),e.styleSheet?e.styleSheet.cssText=e.styleSheet.cssText+t:e.appendChild(n.createTextNode(t))},s.autoLoad&&e(s.coreLib),e.define=e.add,e._config=s,e._mods=s.mods,this.Do=e,g()}();
        }
        function reportTrack(url) {
          if (!url) { return false }
          $.ajax({ url: url, dataType: 'text/html' })
        }
        Do.ready(
            'https://img3.doubanio.com/f/movie/b2a06a0332fc1526f4caaf8c76c2717d24da408d/js/movie/lib/jsrender.min.js',
            function(){
                $(document).on('click', '.cross span', function(e) {
                    var $this = $(this);
                    var $dialog = $this.parents('#tv-play-source');
                    $dialog.remove();
                });
                $('body').bind('click', function(e) {
                    var $this = $(e.target),
                        $source = $('.play-source');
                    if (!$this.is('.playBtn') && !$this.parents('.play-source').length) {
                        $source.remove();
                    }
                });
                var sources = {};
                sources[15] = [
                            {play_link: "https://www.douban.com/link2/?url=https%3A%2F%2Fm.miguvideo.com%2Fmgs%2Fmsite%2Fprd%2Fdetail.html%3Fcid%3D677040723%26pwId%3Dd01197d3076b4164af82983c408bb996&amp;subtype=15&amp;type=online-video&amp;link2key=42fb1da4a8", ep: "1"},
                ];
                sources[1] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F0iwg66rmn19yseb.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video", ep: "1"},
                ];
                sources[9] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_19rrj6sk8k.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video", ep: "1"},
                ];
                sources[8] = [
                            {play_link: "https://www.douban.com/link2/?url=https%3A%2F%2Fwww.bilibili.com%2Fbangumi%2Fplay%2Fss28424%3Fbsource%3Ddouban&amp;subtype=8&amp;type=online-video&amp;link2key=42fb1da4a8", ep: "1"},
                ];
                sources[13] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fvip.1905.com%2Fplay%2F1333716.shtml%3F__hz%3D6e0721b2c6977135%26api_source%3Ddouban_vodadd&amp;subtype=13&amp;type=online-video", ep: "1"},
                ];
                $('.playBtn').each(function(i, item) {
                    // 曝光监测上报
                    if (item) {
                        reportTrack(item.dataset.impressionTrack);
                    }
                });
                $('.playBtn').click(function(e){
                    // 点击监测上报
                    reportTrack(e.target.dataset.clickTrack);
                    
                    $('.play-source').remove();

                    var height, width, tmpl, cn, source;
                    var $dialog = $('#tv-play-source');
                    var $this = $(this);
                    source = $this.data('source');
                    if(!source)return;
                    cn = $this.data('cn');

                    tmpl = $.templates('#episode-tmpl');
                    $dialog = $(tmpl.render({playlist: sources[source], cn: cn}));

                    $dialog.hide();
                    $('body').append($dialog);
                    width = $dialog.outerWidth();

                    $dialog.css({
                        marginLeft: -width / 2,
                        top: $this.offset().top + $this.outerHeight()
                    }).show();
                });
            });
    </script><script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/1d94f76609af2281.js"></script>
    
        <script>
            window._USER_ABNORMAL = {"abnormal":{"status":"S"}}
        </script>
        <script type="text/javascript" src="https://img3.doubanio.com/f/shire/eedd954dfd0fb8d611a30cc1ecafeda9cccfe764/js/abnormal_account.js"></script>
    
    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '264064658',
            browserId = 'DcI5Fbd5RAQ',
            criteria = '7:邱岳峰|7:雷金纳德·加德纳|7:亨利·丹尼尔|7:杰克·奥克|7:美国电影|7:1940|7:剧情|7:宝莲·高黛|7:经典|7:美国|7:比利·吉尔伯特|7:黑白|7:卓别林|7:战争|7:格蕾斯·海尔|7:喜剧|7:黑色幽默|7:查理·卓别林|7:卡特·德黑文|7:CharlesChaplin|3:/subject/1295646/',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle', 'dale_movie_subject_banner_after_intro', 'dale_subject_right_guess_you_like', 'dale_movie_subject_hovering_video'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/MnJwNGlleS9mL2FkanMvY2M1OGQyNTQ2N2I2YmQzOTlmNTliMGJiMjI4MWRhZTlkNTNjYTFkZC9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>











    
  









<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '1', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








      

    <!-- dae-web-movie--default-6b96d487b6-xpk9g-->

  <script>_SPLITTEST=''</script>
</body>

</html>


"""
try:
    movie_soup = BeautifulSoup(douban_html, 'html.parser')
    # 片名
    name = movie_soup.find('span', {'property': 'v:itemreviewed'}).text.split(' ')[0]
    # 上映年份
    year = movie_soup.find('span', {'class': 'year'}).text.replace('(', '').replace(')', '')
    # 评分
    score = movie_soup.find('strong', {'property': 'v:average'}).text
    # 评价人数
    votes = movie_soup.find('span', {'property': 'v:votes'}).text
    # 海报url
    try:
        playbill_link = movie_soup.find('img', {'rel': 'v:image'}).get('src')
    except Exception as error:
        print(error)
        playbill_link = ''
    ## 电影信息
    infos = movie_soup.find('div', {'id': 'info'}).text.split('\n')[1:11]
    # 导演
    director = ','.join(infos[0].split(': ')[1].replace(' ', '').split('/'))
    # 编剧
    scriptwriter = ','.join(infos[1].split(': ')[1].replace(' ', '').split('/'))
    # 主演
    # actor = re.findall(r'[^\'\"]+', ','.join(infos[2].split(': ')[1].replace(' ', '').split('/')))
    actor = ','.join(infos[2].split(': ')[1].replace(' ', '').split('/'))
    actors = []
    for data in [data for data in actor.split(',')]:
        if '\'' in data:
            data = ''.join(data.split('\''))
        actors.append(data)
    actors = ','.join(actors)
    # print(actors)
    # 类型
    movies_type = ','.join(infos[3].split(': ')[1].replace(' ', '').split('/'))
    # 国家/地区
    area = ','.join(infos[4].split(': ')[1].replace(' ', '').split('/'))
    # 语言
    lang = ','.join(infos[5].split(': ')[1].replace(' ', '').split('/'))
    # 上映日期
    release_time = ','.join(infos[6].split(': ')[1].replace(' ', '').split('/'))
    # 电影时长
    movie_long = infos[7].split(': ')[1].replace(' ', '')
    # 短评数量
    short_review_num = re.findall(r'\d+', movie_soup.find('div', {'class': 'mod-hd'}).text.split('\n')[9].replace(' ', ''))[0]
    # 星级占比
    star_compare = ','.join(re.findall(r'\d+.\d+%',''.join(data for data in movie_soup.find('div', {'class': 'ratings-on-weight'}).text.replace(' ', '').split('\n'))))
    # 电影简介
    movie_summary: str = re.findall(f'[^\u3000]+', ''.join(data for data in movie_soup.find('span', {'property': 'v:summary'}).text.replace(' ', '').split('\n')))[0]
    if '\'' in movie_summary or '\"' in movie_summary:
        movie_summary = ''.join(movie_summary.split('\''))
    # 电影短评
    movie_review_data = []
    movie_review = [data.text.replace(' ', '').split('\n') for data in movie_soup.findAll('div', {'class': 'comment'})]
    movie_review_user = []
    movie_review_star = re.findall(r'\d+', ''.join([data.get('class')[0] for data in (movie_soup.findAll('span', {'class': 'rating'}))]))
    movie_review_time = []
    movie_review_comment = []
    for data in movie_review:
        for data_data in data:
            if data_data == '':
                data.remove(data_data)
    for data in movie_review:
        user_msg = ''.join(re.findall(f'[\u4E00-\u9FA5A-Za-z0-9_]+', data[2]))
        if user_msg is None:
            user_msg = 'Anonymous'
        movie_review_time.append(data[4])
        movie_review_user.append(user_msg)
        movie_review_comment.append(''.join(re.findall(f'[^\'\"]+', data[8])))
    for user, stat, time, comment in zip(movie_review_user, movie_review_star, movie_review_time,movie_review_comment):
        movie_review_data.append(json.dumps({'user': f'{user}', 'star': f'{stat}', 'time': f'{time}', 'comment': f'{comment}'}, ensure_ascii=False))
    # 相关图片
    about_img = ','.join([data.get('src') for data in [data.findAll('img') for data in movie_soup.findAll('ul', {'class': 'related-pic-bd'})][0]])
    # 相关视频
    try:
        about_avi = movie_soup.find('a', {'class': 'related-pic-video'}).get('href')
    except Exception as error:
        print(error)
        about_avi = ''
    print(
        name, year, score, votes, playbill_link, director, scriptwriter, actor, movies_type, area, lang, release_time, movie_long,
        short_review_num, star_compare, movie_summary, movie_review_data, about_img
    )
except Exception as error:
    print(error)
    pass

# print(requests.get("http://127.0.0.1:5010/get/").json().get("proxy"))


