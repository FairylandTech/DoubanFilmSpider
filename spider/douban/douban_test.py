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

douban_html = """

<!DOCTYPE html>
<html lang="zh-CN" class="ua-windows ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        圣诞坏公公 (豆瓣)
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
    
    <meta name="keywords" content="圣诞坏公公,Bad Santa,圣诞坏公公影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="圣诞坏公公电影简介和剧情介绍,圣诞坏公公影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/movie/subject/1306858/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/1306858/" />
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
  "name": "圣诞坏公公 Bad Santa",
  "url": "/subject/1306858/",
  "image": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp",
  "director": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1045150/",
      "name": "泰利·茨威戈夫 Terry Zwigoff"
    }
  ]
,
  "author": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1317347/",
      "name": "格伦·费卡拉 Glenn Ficarra"
    }
  ]
,
  "actor": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1025200/",
      "name": "比利·鲍伯·松顿 Billy Bob Thornton"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000290/",
      "name": "托尼·考克斯 Tony Cox"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1168595/",
      "name": "布瑞特·凯利 Brett Kelly"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1031803/",
      "name": "劳伦·格拉汉姆 Lauren Graham"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1025242/",
      "name": "劳伦·汤姆 Lauren Tom"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1374203/",
      "name": "罗娜·斯科特 Lorna Scott"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027201/",
      "name": "伯尼·麦克 Bernie Mac"
    }
  ]
,
  "datePublished": "2003-11-26",
  "genre": ["\u559c\u5267", "\u72af\u7f6a", "\u5267\u60c5"],
  "duration": "PT1H31M",
  "description": "威利（比利·鲍伯·松顿 Billy Bob Thornton 饰）的工作很有趣，每逢圣诞，他便会穿上一身圣诞老人的行头，带着雪白的大胡子对公司的商品进行促销。然而，对于威利来说，这份工作远远没有表面上...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "3222",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "6.9"
  }
}
</script>

    
    
    <meta property="og:title" content="圣诞坏公公 Bad Santa" />
    <meta property="og:description" content="威利（比利·鲍伯·松顿 Billy Bob Thornton 饰）的工作很有趣，每逢圣诞，他便会穿上一身圣诞老人的行头，带着雪白的大胡子对公司的商品进行促销。然而，对于威利来说，这份工作远远没有表面上..." />
    <meta property="og:site_name" content="豆瓣" />
    <meta property="og:url" content="https://movie.douban.com/subject/1306858/" />
    <meta property="og:image" content="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp" />
    <meta property="og:type" content="video.movie" />
            <meta property="video:actor" content="比利·鲍伯·松顿" />
            <meta property="video:actor" content="托尼·考克斯" />
            <meta property="video:actor" content="布瑞特·凯利" />
            <meta property="video:actor" content="劳伦·格拉汉姆" />
            <meta property="video:actor" content="劳伦·汤姆" />
            <meta property="video:actor" content="罗娜·斯科特" />
            <meta property="video:actor" content="伯尼·麦克" />
            <meta property="video:director" content="泰利·茨威戈夫" />
        <meta property="video:duration" content="5460" />


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/25f6c5c6cd31a18b.css">

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
    SSE_TOKEN: "b36b2a1f20085ffe21341279caa1cf413c275570",
    SSE_TIMESTAMP: "1667992856",
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
        <span property="v:itemreviewed">圣诞坏公公 Bad Santa</span>
            <span class="year">(2003)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">
                    
                        



<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/1306858/photos?type=R" title="点击看更多海报">
        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp" title="点击看更多海报" alt="Bad Santa" rel="v:image" />
   </a>
                <p class="gact">
                    <a href="https://movie.douban.com/subject/1306858/edit">
                        更新描述或海报
                    </a>
                </p>
</div>

                    


<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1045150/" rel="v:directedBy">泰利·茨威戈夫</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/subject_search?search_text=Glenn%20Ficarra">Glenn Ficarra</a> / <a href="/subject_search?search_text=John%20Requa">John Requa</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1025200/" rel="v:starring">比利·鲍伯·松顿</a> / <a href="/celebrity/1000290/" rel="v:starring">托尼·考克斯</a> / <a href="/celebrity/1168595/" rel="v:starring">布瑞特·凯利</a> / <a href="/celebrity/1031803/" rel="v:starring">劳伦·格拉汉姆</a> / <a href="/celebrity/1025242/" rel="v:starring">劳伦·汤姆</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">喜剧</span> / <span property="v:genre">犯罪</span><br/>
        <span class="pl">官方网站:</span> <a href="http://www.badsanta-derfilm.de/" rel="nofollow" target="_blank">http://www.badsanta-derfilm.de/</a><br/>
        <span class="pl">制片国家/地区:</span> 美国 / 德国<br/>
        <span class="pl">语言:</span> 英语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2003-11-26">2003-11-26</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="91">91 分钟</span> / 88 分钟(Director's cut) / 98 分钟(unrated version)<br/>
        <span class="pl">又名:</span> 圣诞有贼 / Badder Santa<br/>
        <span class="pl">IMDb:</span> tt0307987<br>

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
    <strong class="ll rating_num" property="v:average">6.9</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar35"></div>
        <div class="rating_sum">
                <a href="comments" class="rating_people">
                    <span property="v:votes">3222</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:13px"></div>
        <span class="rating_per">10.4%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:42px"></div>
        <span class="rating_per">32.6%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">48.5%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:9px"></div>
        <span class="rating_per">6.9%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:2px"></div>
        <span class="rating_per">1.7%</span>
        <br />
        </div>
</div>

    </div>
        
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=喜剧&type=24&interval_id=45:35&action=">41% 喜剧片</a><br/>
            好于 <a href="/typerank?type_name=犯罪&type=3&interval_id=50:40&action=">48% 犯罪片</a><br/>
        </div>
</div>


                
            </div>
            
                





<div id="interest_sect_level" class="clearfix">
        
            <a href="https://movie.douban.com/subject/1306858/?interest=wish&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-1306858-wish">
                <span>想看</span>
            </a>
            <a href="https://movie.douban.com/subject/1306858/?interest=collect&amp;ck=F6Lh" rel="nofollow" class="cls_abnormal colbutt ll" name="pbtn-1306858-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1306858-collect-1">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1306858-collect-2">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1306858-collect-3">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1306858-collect-4">
            <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/>
        </a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1306858-collect-5">
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
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt'})" href="javascript:;" class="j a_collect_btn" name="cbtn-1306858">写短评</a>
 </li>
                  <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv'})" class="cls_abnormal" href="https://movie.douban.com/subject/1306858/new_review" rel="nofollow">写影评</a>
 </li>
                    <li> 
        


  <link rel="stylesheet" href="https://img3.doubanio.com/f/sns/9919c071eab1c25bc462d58a582feb79e3867be4/css/sns/doulist/new_doulist_button.css">
    <div class="doulist-add-btn">

  

  
  <a href="javascript:void(0)"
     data-id="1306858"
     data-cate="1002"
     data-canview="True"
     data-url="https://movie.douban.com/subject/1306858/"
     data-catename="电影"
     data-link="https://www.douban.com/people/264064658/doulists/all?add=1306858&amp;cat=1002"
     data-title="圣诞坏公公 Bad Santa"
     data-picture="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp"
     class="lnk-doulist-add"
     onclick="moreurl(this, { 'from':'doulist-btn-1002-1306858-264064658'})">
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
   

   
    
    <span class="rec" id="电影-1306858">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/1306858/"
        data-desc="电影《圣诞坏公公 Bad Santa》 (来自豆瓣) "
        data-title="电影《圣诞坏公公 Bad Santa》 (来自豆瓣) "
        data-pic="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.jpeg"
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
                <input type="hidden" name="target-id" value="1306858">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="圣诞坏公公 Bad Santa‎ (2003)">
                <input type="hidden" name="desc" value="导演 泰利·茨威戈夫 主演 比利·鲍伯·松顿 / 托尼·考克斯 / 美国 / 德国 / 6.9分(3222评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp" />
                <strong>圣诞坏公公 Bad Santa‎ (2003)</strong>
                <p>导演 泰利·茨威戈夫 主演 比利·鲍伯·松顿 / 托尼·考克斯 / 美国 / 德国 / 6.9分(3222评价)</p>
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
            share-id="1306858" 
            data-mode="plain" data-name="圣诞坏公公 Bad Santa‎ (2003)" 
            data-type="movie" data-desc="导演 泰利·茨威戈夫 主演 比利·鲍伯·松顿 / 托尼·考克斯 / 美国 / 德国 / 6.9分(3222评价)" 
            data-href="https://movie.douban.com/subject/1306858/" data-image="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1546893397.webp" 
            data-properties="{}" 
            data-redir="" data-text="" 
            data-apikey="" data-curl="" 
            data-count="10" data-object_kind="1002" 
            data-object_id="1306858" data-target_type="rec" 
            data-target_action="0" 
            data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/1306858\/&#34;,&#34;subject_title&#34;:&#34;圣诞坏公公 Bad Santa‎ (2003)&#34;}">推荐</a>
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
            


    <div id="collect_form_1306858"></div>


        



<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">圣诞坏公公的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report-intra">
                    
                        <span property="v:summary" class="">
                                　　威利（比利·鲍伯·松顿 Billy Bob Thornton 饰）的工作很有趣，每逢圣诞，他便会穿上一身圣诞老人的行头，带着雪白的大胡子对公司的商品进行促销。然而，对于威利来说，这份工作远远没有表面上看起来的那么简单，每一年的这个时候，除了欢度佳节，还是他和他的伙伴马库斯（托尼·考克斯 Tony Cox 饰）大赚一笔的最佳时刻，他的真正身份是一个小偷。
                                    <br />
                                　　今年和往年一样，可又有些不同。威利的诡异行踪遭到了精明的保安金（伯尼·麦克 Bernie Mac 饰）的怀疑，同时，百货公司的经理鲍勃（约翰·雷特尔 John Ritter 饰）也变成了难缠的人物。更让威利感到抓狂的是，一个8岁的小男孩盯上了他。在重重地阻力面前，威利的行动能否成功呢？
                        </span>
                        <span class="pl"><a href="https://movie.douban.com/help/movie#t0-qs">&copy;豆瓣</a></span>
            </div>
</div>


    <div id="dale_movie_subject_banner_after_intro"></div>

    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">圣诞坏公公的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/1306858/celebrities">全部 22</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1045150/" title="泰利·茨威戈夫 Terry Zwigoff" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/raw/public/p21657.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1045150/" title="泰利·茨威戈夫 Terry Zwigoff" class="name">泰利·茨威戈夫</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1025200/" title="比利·鲍伯·松顿 Billy Bob Thornton" class="">
      <div class="avatar" style="background-image: url(https://img9.doubanio.com/view/celebrity/raw/public/p1423398311.6.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1025200/" title="比利·鲍伯·松顿 Billy Bob Thornton" class="name">比利·鲍伯·松顿</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1000290/" title="托尼·考克斯 Tony Cox" class="">
      <div class="avatar" style="background-image: url(https://img9.doubanio.com/view/celebrity/raw/public/p1480299695.55.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1000290/" title="托尼·考克斯 Tony Cox" class="name">托尼·考克斯</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1168595/" title="布瑞特·凯利 Brett Kelly" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p55503.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1168595/" title="布瑞特·凯利 Brett Kelly" class="name">布瑞特·凯利</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1031803/" title="劳伦·格拉汉姆 Lauren Graham" class="">
      <div class="avatar" style="background-image: url(https://img2.doubanio.com/view/celebrity/raw/public/p1618767686.43.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1031803/" title="劳伦·格拉汉姆 Lauren Graham" class="name">劳伦·格拉汉姆</a></span>

      <span class="role" title="演员">演员</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1025242/" title="劳伦·汤姆 Lauren Tom" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/raw/public/p41820.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1025242/" title="劳伦·汤姆 Lauren Tom" class="name">劳伦·汤姆</a></span>

      <span class="role" title="演员">演员</span>

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
      SUBJECT_ID: '1306858',
      USER_ID: '264064658'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/82d2333c56fe1813ad6ee312f35a915941d906ae/entry_creator/dist/author_subject/index.js"></script>


    
        










    
    <div id="related-pic" class="related-pic">
        
    
    
    <h2>
        <i class="">圣诞坏公公的图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/video/create?subject_id=1306858">添加视频评论</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/1306858/all_photos">图片49</a>&nbsp;·&nbsp;<a href="https://movie.douban.com/subject/1306858/mupload">添加</a>
            )
            </span>
    </h2>


        <ul class="related-pic-bd  ">
                <li>
                    <a href="https://movie.douban.com/photos/photo/1353026364/"><img src="https://img9.doubanio.com/view/photo/sqxs/public/p1353026364.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2277820106/"><img src="https://img9.doubanio.com/view/photo/sqxs/public/p2277820106.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2277820102/"><img src="https://img2.doubanio.com/view/photo/sqxs/public/p2277820102.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2574491652/"><img src="https://img2.doubanio.com/view/photo/sqxs/public/p2574491652.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2277820109/"><img src="https://img1.doubanio.com/view/photo/sqxs/public/p2277820109.webp" alt="图片" /></a>
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


<div class="mod">
    <div class="hd">
        
    <h2>
        <i class="">圣诞坏公公的获奖情况</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1306858/awards/">全部</a>
            )
            </span>
    </h2>

    </div>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/golden-globes/61/">第61届金球奖</a>
            </li>
            <li>电影类 音乐/喜剧片最佳男主角(提名)</li>
            <li><a href='https://movie.douban.com/celebrity/1025200/' target='_blank'>比利·鲍伯·松顿</a></li>
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
                <a href="https://movie.douban.com/subject/10594840/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2385533564.webp" alt="圣诞坏公公2" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/10594840/?from=subject-page" class="" >圣诞坏公公2</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1298318/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2358937645.webp" alt="乞丐皇帝" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1298318/?from=subject-page" class="" >乞丐皇帝</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1298884/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2328716218.webp" alt="我的表兄维尼" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1298884/?from=subject-page" class="" >我的表兄维尼</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1308864/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p840341316.webp" alt="我爱哈克比" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1308864/?from=subject-page" class="" >我爱哈克比</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1875488/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1452354753.webp" alt="冰刀双人组" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1875488/?from=subject-page" class="" >冰刀双人组</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1308822/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p811665017.webp" alt="猪头逛大街" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1308822/?from=subject-page" class="" >猪头逛大街</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292635/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2505000763.webp" alt="夜迷情" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292635/?from=subject-page" class="" >夜迷情</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1306445/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2652019713.webp" alt="超级骑警" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1306445/?from=subject-page" class="" >超级骑警</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1300947/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p794190927.webp" alt="拯救格雷斯" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1300947/?from=subject-page" class="" >拯救格雷斯</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1297619/?from=subject-page" >
                    <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2648672981.webp" alt="欲望小镇" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1297619/?from=subject-page" class="" >欲望小镇</a>
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
            
            
        <a class="comment_btn j a_collect_btn" name="cbtn-1306858" href="javascript:;" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">圣诞坏公公的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1306858/comments?status=P">全部 798 条</a>
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
            
    

        
        <div class="comment-item " data-cid="757867520">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">3</span>

                    <input value="757867520" type="hidden"/>
                    <a href="javascript:;" data-id="757867520"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/56090186/" class="">古都孤独Z inc</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2013-12-26 21:46:21">
                    2013-12-26 21:46:21
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">真的很难吸引人，坏公公从头到尾飙脏话，很难想象是一部迪士尼产品的电影，科恩兄弟的元素也不多，幸好结尾还算温馨，否则也很难对得起喜剧的称号。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1306858/?comment_id=757867520"></div>
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
        
        <div class="comment-item " data-cid="331010911">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">1</span>

                    <input value="331010911" type="hidden"/>
                    <a href="javascript:;" data-id="331010911"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/1856756/" class="">sandy</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2010-12-25 10:32:20">
                    2010-12-25 10:32:20
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">平安夜就是这样度过的。
前半段在铺垫，看得倒认真。后来帮助小男孩成长，才是转折的开始；可惜跟爹妈打牌了。
虽然有感动，但还是闷了些，也许是我浮躁了。</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1306858/?comment_id=331010911"></div>
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
        
        <div class="comment-item " data-cid="296437829">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">3</span>

                    <input value="296437829" type="hidden"/>
                    <a href="javascript:;" data-id="296437829"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/infero/" class="">HurryShit</a>
                    <span>看过</span>
                    <span class="allstar20 rating" title="较差"></span>
                <span class="comment-time " title="2010-09-23 12:01:29">
                    2010-09-23 12:01:29
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">不少兒童不宜的對話及動作場面，某種程度上可視為《34街奇蹟》的邪惡雙胞胎（部分情節設計相似）。顛覆之處除語言、角色設計外，更強烈的是直接說「聖誕老人不存在」。這對大男孩 vs. 小男孩的救贖，不在宗教信仰，在於人與人間聯繫出的「家庭」可能性，但這說穿了也是美國獨立製片的老梗母題…</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1306858/?comment_id=296437829"></div>
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
        
        <div class="comment-item " data-cid="2548607">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">10</span>

                    <input value="2548607" type="hidden"/>
                    <a href="javascript:;" data-id="2548607"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/iamseven/" class="">jijo</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2006-04-21 07:13:45">
                    2006-04-21 07:13:45
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">不管别人怎么看!我就是无比喜欢此片</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1306858/?comment_id=2548607"></div>
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
        
        <div class="comment-item " data-cid="310647217">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                    <span class="votes vote-count">0</span>

                    <input value="310647217" type="hidden"/>
                    <a href="javascript:;" data-id="310647217"
                        class="j cls_abnormal" 
                        onclick="">有用</a>
                    
                <!-- 删除短评 -->
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/jessica.jia/" class="">JS</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2010-11-02 20:06:10">
                    2010-11-02 20:06:10
                </span>
                <span class="comment-location"></span>
            </span>
        </h3>
        <p class=" comment-content">
            
                <span class="short">五星没有分类，只能折中了。喜欢结局，还有那句 do you really need all that shit? 我还是讨厌丫随便骂小孩！</span>
        </p>
        <div class="comment-report" data-url="https://movie.douban.com/subject/1306858/?comment_id=310647217"></div>
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
                            798条
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
                    data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/1306858/new_review">
                    <span>我要写影评</span>
                </a>
            <h2>
                    圣诞坏公公的影评 · · · · · ·

                    <span class="pl">( <a href="reviews">全部 14 条</a> )</span>
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
        
    

            
    
    <div data-cid="1029186">
        <div class="main review-item" id="1029186">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/wowo/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u1071525-1.jpg">
        </a>

        <a href="https://www.douban.com/people/wowo/" class="name">蜗蜗</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2006-03-04" class="main-meta">2006-03-04 12:37:31</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1029186/">Bad Santa－生活多残酷</a></h2>

                <div id="review_1029186_short" class="review-short" data-rid="1029186">
                    <div class="short-content">

                        这不能算一部好看的片子，虽然有个还算光明的尾巴。之所以看完了，是因为在影片的前80分钟我一直在提醒自己两件事情： 1。生活是残酷的。我很幸运不用面对如此残酷的现实，那么起码我可以忍耐一下这部电影。 2。也许我可以期待一个比较好点的结尾。就象Adaptation（兰花窃贼）...

                        &nbsp;(<a href="javascript:;" id="toggle-1029186-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1029186_full" class="hidden">
                    <div id="review_1029186_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1029186" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1029186">
                                8
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1029186" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1029186">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1029186/#comments" class="reply cls_abnormal">4回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="1072612">
        <div class="main review-item" id="1072612">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/lululuna/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1249444-20.jpg">
        </a>

        <a href="https://www.douban.com/people/lululuna/" class="name">½luna</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2006-09-09" class="main-meta">2006-09-09 17:28:10</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1072612/">另类圣诞老人</a></h2>

                <div id="review_1072612_short" class="review-short" data-rid="1072612">
                    <div class="short-content">

                        应该慈祥的圣诞老人怎么这样了 吃喝嫖赌 道德败坏 无药可救 整个一败类  弱智小孩本来就不是都傻兮兮的 单纯懦弱 善良纯朴 简单执着  他感动人心  至少 他感动了一个无药可救的败类   所以 败类不再无药可救 因为 他还可以被感动 所以 弱智并不智力低下 因为 他是最最无邪的  ...

                        &nbsp;(<a href="javascript:;" id="toggle-1072612-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1072612_full" class="hidden">
                    <div id="review_1072612_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1072612" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1072612">
                                4
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1072612" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1072612">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1072612/#comments" class="reply cls_abnormal">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="5229159">
        <div class="main review-item" id="5229159">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/31634588/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u31634588-5.jpg">
        </a>

        <a href="https://www.douban.com/people/31634588/" class="name">行尸走肉</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2011-12-25" class="main-meta">2011-12-25 13:37:15</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/5229159/">每个圣人都有过去，每个罪人都有未来</a></h2>

                <div id="review_5229159_short" class="review-short" data-rid="5229159">
                    <div class="short-content">

                        每个圣人都有过去，每个罪人都有未来。 好和坏有时候是没有严格界限的。 圣诞坏公公偷窃、破坏、和女人做爱，就是坏的吗？他为了遵守礼物的诺言倒在子弹下，就是好的吗？ 神说，不要用道德标准去评判人。 耶稣甚至说，永远不要去评判人。 人，以不信、轻蔑和苦毒赤裸裸地表明自...

                        &nbsp;(<a href="javascript:;" id="toggle-5229159-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_5229159_full" class="hidden">
                    <div id="review_5229159_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="5229159" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-5229159">
                                2
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="5229159" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-5229159">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/5229159/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="1360884">
        <div class="main review-item" id="1360884">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/2408283/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u2408283-2.jpg">
        </a>

        <a href="https://www.douban.com/people/2408283/" class="name">glide</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2008-04-23" class="main-meta">2008-04-23 23:18:01</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1360884/">儿童不宜的圣诞题材</a></h2>

                <div id="review_1360884_short" class="review-short" data-rid="1360884">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        08年才来评论03年的片子似乎有点晚,不过从我是刚从chd下到就看起来了,因为看简介觉得应该是挺有意思的片子.我喜欢喜剧,喜欢看电影少些思考和猜测.这就是这么一部片子. 特别喜欢里面&#34;金&#34;向两个小贼勒索50%的那个桥段,我和我老婆几乎笑翻在地,那个黑人演员把贪婪和得意演绎得入木...

                        &nbsp;(<a href="javascript:;" id="toggle-1360884-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1360884_full" class="hidden">
                    <div id="review_1360884_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1360884" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1360884">
                                2
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1360884" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1360884">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1360884/#comments" class="reply cls_abnormal">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="13014741">
        <div class="main review-item" id="13014741">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/157283896/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u157283896-6.jpg">
        </a>

        <a href="https://www.douban.com/people/157283896/" class="name">迷离幻境</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2020-11-28" class="main-meta">2020-11-28 02:06:36</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/13014741/">是一部娱乐电影，喜剧电影，救赎电影，快餐电影。但是很温暖，很单纯。</a></h2>

                <div id="review_13014741_short" class="review-short" data-rid="13014741">
                    <div class="short-content">

                        是一部娱乐电影，喜剧电影，救赎电影，快餐电影。但是很温暖，很单纯。 童话故事，我喜欢童话喜剧。显然这是一个童话喜剧。我喜欢这一部电影，显然这不是什么关于人生哲学思考的。啊，童话，总是在告诉你真理却又不会真的逼着你做什么。 这总是童话，童话说，你可以沉浸于幻境...

                        &nbsp;(<a href="javascript:;" id="toggle-13014741-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_13014741_full" class="hidden">
                    <div id="review_13014741_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="13014741" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-13014741">
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="13014741" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-13014741">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/13014741/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="8278782">
        <div class="main review-item" id="8278782">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/120570973/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u120570973-11.jpg">
        </a>

        <a href="https://www.douban.com/people/120570973/" class="name">JJw</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2017-01-07" class="main-meta">2017-01-07 10:53:15</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/8278782/">希望你我都能碰到一个像小胖子一样的天使</a></h2>

                <div id="review_8278782_short" class="review-short" data-rid="8278782">
                    <div class="short-content">

                        一直以为是一部关于圣诞老人的温馨喜剧  毕竟有关圣诞的电影都很暖 结果。。。看了半个小时简直颠覆了我的所有设想      偷窃、酗酒、乱搞、对小孩都是脏话连篇 但是小胖子的出现让电影发生转折 始终相信人性本善，每个人天生就是善良的，只不过由于经历的越多，黑暗面就会越宽...

                        &nbsp;(<a href="javascript:;" id="toggle-8278782-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_8278782_full" class="hidden">
                    <div id="review_8278782_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="8278782" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-8278782">
                                1
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="8278782" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-8278782">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/8278782/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="7113597">
        <div class="main review-item" id="7113597">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/2854129/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u2854129-2.jpg">
        </a>

        <a href="https://www.douban.com/people/2854129/" class="name">甜芦黍</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2014-09-28" class="main-meta">2014-09-28 17:03:36</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/7113597/">圣诞坏公公</a></h2>

                <div id="review_7113597_short" class="review-short" data-rid="7113597">
                    <div class="short-content">

                        白雪纷飞、铜铃清响，划过长空的是麋鹿，是礼物，是圣诞老人，更是每个孩子对于这个节日的期盼。可是，就有这么一位不把孩子们的梦想当回事的成年人，不好好地在打工的商场里给孩子讲故事，发礼物，只知道把妹。在他如人渣般的生活中，却又因为“圣诞老人”的职责而发生改变。...

                        &nbsp;(<a href="javascript:;" id="toggle-7113597-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_7113597_full" class="hidden">
                    <div id="review_7113597_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="7113597" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-7113597">
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="7113597" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-7113597">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/7113597/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="1365978">
        <div class="main review-item" id="1365978">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/2267024/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u2267024-4.jpg">
        </a>

        <a href="https://www.douban.com/people/2267024/" class="name">不为彼岸</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2008-04-29" class="main-meta">2008-04-29 09:06:53</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1365978/">很颓废的一部片子</a></h2>

                <div id="review_1365978_short" class="review-short" data-rid="1365978">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        片子看了将近一个小时没看懂什么意思，知道下半部分出现了那个胖小子才明白了本片的主旨，说是圣诞老公公，但是小孩看了学不好，完全颠覆圣诞老人的形象，吃喝嫖赌抽，坑蒙拐骗偷，样样在行。不过还是为他们戏剧性的配合偷窃叫好，尤其是那个小矮人，很可爱，从扶梯中间滑下来...

                        &nbsp;(<a href="javascript:;" id="toggle-1365978-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1365978_full" class="hidden">
                    <div id="review_1365978_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1365978" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1365978">
                                1
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1365978" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1365978">
                                2
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1365978/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

            
    
    <div data-cid="1581231">
        <div class="main review-item" id="1581231">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/champange/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u2822124-25.jpg">
        </a>

        <a href="https://www.douban.com/people/champange/" class="name">Listen-22</a>

            <span class="allstar10 main-title-rating" title="很差"></span>

        <span content="2008-12-11" class="main-meta">2008-12-11 18:42:20</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1581231/">just a POS</a></h2>

                <div id="review_1581231_short" class="review-short" data-rid="1581231">
                    <div class="short-content">

                        I don&#39;t know why our teacher showed this moive to us. It sucks. She is a catholic, how could she stand so much dirty words in the moive. I don&#39;t know whether American parents will let their children watch it or not.But I don&#39;t think that show this moive to ...

                        &nbsp;(<a href="javascript:;" id="toggle-1581231-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1581231_full" class="hidden">
                    <div id="review_1581231_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1581231" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1581231">
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1581231" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1581231">
                                4
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1581231/#comments" class="reply cls_abnormal">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>


        <div class="fold-hd">
                <a class="btn-unfold" href="#">有一些影评被折叠了</a>
                    <a class="qa" href="https://help.douban.com/opinion?app=movie#t1-q2">为什么被折叠？</a>
            <div class="qa-tip">评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。</div>
        </div>
        <div class="fold-bd">
                
    
    <div data-cid="5710024">
        <div class="main review-item" id="5710024">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/itssuetalking/" class="avator">
            <img width="24" height="24" src="https://img2.doubanio.com/icon/u1629309-2.jpg">
        </a>

        <a href="https://www.douban.com/people/itssuetalking/" class="name">Sue</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2012-12-23" class="main-meta">2012-12-23 11:45:58</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/5710024/">Bad Santa &amp; Bad Teacher</a></h2>

                <div id="review_5710024_short" class="review-short" data-rid="5710024">
                    <div class="short-content">

                        圣诞又要叮叮当叮叮当地到来了，今年我终于放弃了看第101遍真爱至上的想法，转而看了这部Bad Santa。一个自我放逐专长是开保险柜的贼，一个爸爸因为挪用公款被抓无人照料整天被校霸欺负的胖男孩，隐藏在整个作案阴谋背后主使的侏儒小矮人。整部电影节奏都很平缓，每一句台词恨...

                        &nbsp;(<a href="javascript:;" id="toggle-5710024-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_5710024_full" class="hidden">
                    <div id="review_5710024_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="5710024" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-5710024">
                                4
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="5710024" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-5710024">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/5710024/#comments" class="reply cls_abnormal">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
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
                                14篇
                        </a>
                </p>
    </section>
<!-- COLLECTED JS -->




    <br/>

    
            <div class="section-discussion">
                    
                    <div class="mod-hd">
                            <a class="comment_btn cls_abnormal" href="/subject/1306858/discussion/create" rel="nofollow"><span>添加新讨论</span></a>
                        
    <h2>
        讨论区
         &nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;
    </h2>

                    </div>
                    
  <table class="olt"><tr><td><td><td><td></tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1306858/discussion/17525820/" title="为啥在科恩的套盘里有这片儿？">为啥在科恩的套盘里有这片儿？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/water-is-nobody/">water</a></td>
          <td class="pl"><span>3 回应</span></td>
          <td class="pl"><span>2012-03-22 13:39:40</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1306858/discussion/1060164/" title="billy bob kills santa">billy bob kills santa</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/biscuiter/">小饼干在法国</a></td>
          <td class="pl"><span></span></td>
          <td class="pl"><span>2007-04-06 16:50:34</span></td>
        </tr>
  </table>

                    <p class="pl" align="right">
                        <a href="/subject/1306858/discussion/" rel="nofollow">
                            &gt; 去这部影片的讨论区（全部2条）
                        </a>
                    </p>
            </div>

        
    
        
                
                    





<div id="askmatrix">
    <div class="mod-hd">
        <h2>
                关于《圣诞坏公公》的问题
                · · · · · ·
            <span class="pl">
                (<a href='https://movie.douban.com/subject/1306858/questions/?from=subject'>
                    全部1个
                </a>)
            </span>
        </h2>


        <!-- 
    
    <a class='cls_abnormal comment_btn'
        href='https://movie.douban.com/subject/1306858/questions/ask/?from=subject'>我来提问</a>
 -->
    </div>

    <div class="mod-bd">
        <ul class="">
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/1306858/questions/735297/?from=subject" class="">
                            有人能翻译一下小孩最后t恤上写的英文吗？
                    </a>
                </span>
                <span class="meta">
                    1人回答
                </span>
            </li>
        </ul>

        <p>&gt;
            <a href='https://movie.douban.com/subject/1306858/questions/?from=subject'>
                全部1个问题
            </a>
        </p>

    </div>
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

        <a href="/subject/1306858/report_subject_error?pname=在线观看" target="_blank" rel="nofollow" class="report-error">报错</a>
    
    <ul class="bs">
                
                <li>
                        <a class="playBtn" data-cn="腾讯视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1306858&amp;video_type=movie&amp;video_id=192423&amp;source=qq&amp;user_id=264064658&amp;bid=fKbSfr_nyXU&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1306858&amp;video_type=movie&amp;video_id=192423&amp;source=qq&amp;user_id=264064658&amp;bid=fKbSfr_nyXU&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F6rf9wepyd0booay.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video" target="_blank">
                            腾讯视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>
                
                <li>
                        <a class="playBtn" data-cn="爱奇艺视频" data-impression-track="https://frodo.douban.com/rohirrim/video_tracking/impression?subject_id=1306858&amp;video_type=movie&amp;video_id=366583&amp;source=iqiyi&amp;user_id=264064658&amp;bid=fKbSfr_nyXU&amp;platform=pc&amp;location=vendor_subject" data-click-track="https://frodo.douban.com/rohirrim/video_tracking/click?subject_id=1306858&amp;video_type=movie&amp;video_id=366583&amp;source=iqiyi&amp;user_id=264064658&amp;bid=fKbSfr_nyXU&amp;platform=pc&amp;location=vendor_subject" href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_19rrjr1mq8.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video" target="_blank">
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
                <a href="https://movie.douban.com/subject/1306858/doulists">全部</a>
            )
            </span>
    </h2>


    
    <ul>
            
                <li>
                    <a href="https://www.douban.com/doulist/587777/" target="_blank">收集二流屎尿屁和非屎尿屁喜剧电影</a>
                    <span>(窜)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/199924/" target="_blank">【亲爱的圣诞】—— 圣诞特辑</a>
                    <span>(狷介有乌青)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/90486/" target="_blank">Milk週刊的WASTELAND TREASURES專欄(已完结)</a>
                    <span>(爱慕肚滑)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/36859958/" target="_blank">享受你的阴暗面</a>
                    <span>(无定)</span>
                </li>
            
                <li>
                    <a href="https://www.douban.com/doulist/175599/" target="_blank">与超市有关的电影</a>
                    <span>(斯多亞)</span>
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
                <a href="https://www.douban.com/people/264285104/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u264285104-1.jpg" class="pil" alt="清酒一刀c">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/264285104/" class="">清酒一刀c</a>
                    <div class="">
                        今天下午
                        看过
                        
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/210168636/" class="others-interest-avatar">
                    <img src="https://img2.doubanio.com/icon/u210168636-1.jpg" class="pil" alt="紫薇">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/210168636/" class="">紫薇</a>
                    <div class="">
                        昨天
                        看过
                        
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/137102800/" class="others-interest-avatar">
                    <img src="https://img1.doubanio.com/icon/u137102800-7.jpg" class="pil" alt="阿姬👧">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/137102800/" class="">阿姬👧</a>
                    <div class="">
                        昨天
                        看过
                        <span class="allstar30" title="还行"></span>
                    </div>
                </div>
            </li>
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/1306858/comments?status=P">4652人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/1306858/comments?status=F">2095人想看</a>
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

    
<p class="pl">订阅圣诞坏公公的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/1306858/reviews"> feed: rss 2.0</a></span></p>


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
                sources[1] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F6rf9wepyd0booay.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video", ep: "1"},
                ];
                sources[9] = [
                            {play_link: "https://www.douban.com/link2/?url=http%3A%2F%2Fwww.iqiyi.com%2Fv_19rrjr1mq8.html%3Fvfm%3Dm_331_dbdy%26fv%3D4904d94982104144a1548dd9040df241&amp;subtype=9&amp;type=online-video", ep: "1"},
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
    </script><script type="text/javascript">
        ;/*
 * jQuery hashchange event - v1.3 - 7/21/2010
 * http://benalman.com/projects/jquery-hashchange-plugin/
 * 
 * Copyright (c) 2010 "Cowboy" Ben Alman
 * Dual licensed under the MIT and GPL licenses.
 * http://benalman.com/about/license/
 */
(function($,e,b){var c="hashchange",h=document,f,g=$.event.special,i=h.documentMode,d="on"+c in e&&(i===b||i>7);function a(j){j=j||location.href;return"#"+j.replace(/^[^#]*#?(.*)$/,"$1")}$.fn[c]=function(j){return j?this.bind(c,j):this.trigger(c)};$.fn[c].delay=50;g[c]=$.extend(g[c],{setup:function(){if(d){return false}$(f.start)},teardown:function(){if(d){return false}$(f.stop)}});f=(function(){var j={},p,m=a(),k=function(q){return q},l=k,o=k;j.start=function(){p||n()};j.stop=function(){p&&clearTimeout(p);p=b};function n(){var r=a(),q=o(m);if(r!==m){l(m=r,q);$(e).trigger(c)}else{if(q!==m){location.href=location.href.replace(/#.*/,"")+q}}p=setTimeout(n,$.fn[c].delay)}$.browser.msie&&!d&&(function(){var q,r;j.start=function(){if(!q){r=$.fn[c].src;r=r&&r+a();q=$('<iframe tabindex="-1" title="empty"/>').hide().one("load",function(){r||l(a());n()}).attr("src",r||"javascript:0").insertAfter("body")[0].contentWindow;h.onpropertychange=function(){try{if(event.propertyName==="title"){q.document.title=h.title}}catch(s){}}}};j.stop=k;o=function(){return a(q.location.href)};l=function(v,s){var u=q.document,t=$.fn[c].domain;if(v!==s){u.title=h.title;u.open();t&&u.write('<script>document.domain="'+t+'"<\/script>');u.close();q.location.hash=v}}})();return j})()})(jQuery,this);

        Douban&&Douban.init_vote_comment&&(Douban.init_vote_comment=function(o){var t=$(o).prev().prev(),n=$(o).prev().val();$(o).click(function(){$.postJSON_withck("/j/comment/vote",{id:n},function(o){0===o.r&&o.count?t.text(o.count):1===o.r&&alert(o.msg)})})}),$(".vote-comment").hover(function(){$(".pop").hide(),$(this).next(".pop").show()},function(){$(".pop").hide()});
        $(function(){
            var UA = navigator.userAgent.toLowerCase();
            isSafari = /safari/.test(UA)
            $("#season").live('change', function(){
                var subjectId = $(this).val();
                if (subjectId.length){
                    window.location = "/subject/" + subjectId + "/";
                    // fix null state bug in Safari
                    if (isSafari) {
                        window.history.pushState &&
                          window.history.pushState(null, document.title, window.location.href)
                    }
                }
            });
            $("#season").val("1306858")

            $(window).hashchange();
            if(window.location.href.indexOf('suggest')>0 && window.location.href.indexOf("?")>0){
                if(window.history.pushState){
                    window.history.pushState(null, document.title, window.location.href.substring(0,window.location.href.indexOf("?")));
                }
            }

            $('.indent .a_show_full').click(function(){
                $.get('/blank?expand');
            });

            $('body').on('click', 'a.write_review', function(e) {
                e.preventDefault();
                if(window._USER_ABNORMAL) {
                    show_abnormal && show_abnormal()
                }else {
                    location.href = $(this).attr('href')
                }
            })
        });
    </script>
    
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
            browserId = 'fKbSfr_nyXU',
            criteria = '7:比利·鲍伯·松顿|7:托尼·考克斯|7:布瑞特·凯利|7:犯罪|7:劳伦·汤姆|7:成长|7:罗娜·斯科特|7:泰利·茨威戈夫|7:圣诞|7:2003|7:美国|7:伯尼·麦克|7:劳伦·格拉汉姆|7:喜剧|7:剧情|7:温情|7:人性|7:黑色幽默|3:/subject/1306858/',
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
    director = ''
    actors = ''
    movies_type = ''
    area = ''
    lang = ''
    release_time = ''
    movie_long = ''
    for info in infos:
        if '导演:' in info :
            director = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
            if '\'' in director:
                director = ''.join(director.split('\''))
        elif '主演:' in info:
            actor = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
            actors = []
            for data in [data for data in actor.split(',')]:
                if '\'' in data:
                    data = ''.join(data.split('\''))
                actors.append(data)
            actors = ','.join(actors)
        elif '类型:' in info:
            movies_type = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
        elif '制片国家/地区:' in info:
            area = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
        elif '语言:' in info:
            lang = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
        elif '上映日期:' in info:
            release_time = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
        elif '片长:' in info:
            movie_long = ','.join(info.split(': ')[1].replace(' ', '').split('/'))
            if '\'' in movie_long:
                movie_long = ''.join(movie_long.split('\''))
    # 导演
    # director = ','.join(infos[0].split(': ')[1].replace(' ', '').split('/'))
    # 编剧
    # scriptwriter = ','.join(infos[1].split(': ')[1].replace(' ', '').split('/'))
    # 主演
    # actor = re.findall(r'[^\'\"]+', ','.join(infos[2].split(': ')[1].replace(' ', '').split('/')))
    # actor = ','.join(infos[2].split(': ')[1].replace(' ', '').split('/'))
    # actors = []
    # for data in [data for data in actor.split(',')]:
    #     if '\'' in data:
    #         data = ''.join(data.split('\''))
    #     actors.append(data)
    # actors = ','.join(actors)
    # print(actors)
    # 类型
    # movies_type = ','.join(infos[3].split(': ')[1].replace(' ', '').split('/'))
    # 国家/地区
    # area = ','.join(infos[4].split(': ')[1].replace(' ', '').split('/'))
    # 语言
    # lang = ','.join(infos[5].split(': ')[1].replace(' ', '').split('/'))
    # 上映日期
    # release_time = ','.join(infos[6].split(': ')[1].replace(' ', '').split('/'))
    # 电影时长
    # movie_long = infos[7].split(': ')[1].replace(' ', '')
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
        name, year, score, votes, playbill_link, director, actors, movies_type, area, lang, release_time, movie_long,
        short_review_num, star_compare, movie_summary, movie_review_data, about_img
    )
except Exception as error:
    print(error)
    pass

# print(requests.get("http://127.0.0.1:5010/get/").json().get("proxy"))


