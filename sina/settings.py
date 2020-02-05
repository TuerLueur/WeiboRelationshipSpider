# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'cookie': '_T_WM=74c160285874b164fd8599e1bcccd563; ALF=1583379185; SCF=AkgbgOD8zh62sy_EYo5W2fMw9ZBRORKniJgg1j4LAY-4FUcQ9axOnO0HahDyyjOkFL9ZUp3JCulnEaytyJX3ugA.; SUB=_2A25zPJYCDeRhGeVH41AX-CbOwjiIHXVQ3jpKrDV6PUJbktANLVr-kW1NTzyo7SU0BEWUzvcPXQJ8QpDvu7mFQhxS; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWCN2ORE8jMZxzFHeVdY7Mg5JpX5K-hUgL.Foe41hzc1hnE1KB2dJLoI7L-UgHEKGHLUPzt; SUHB=04Weq-bGY-Rqs7; SSOLoginState=1580787282'
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'
