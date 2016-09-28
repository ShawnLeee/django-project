# encoding: utf-8
from bs4 import BeautifulSoup
import urllib2
import enum
from api_v_1_0 import User, Comment, Article


USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
BASE_URL = 'http://www.qiushibaike.com/'
MAX_PAGE = 35

class Page_Type(enum):
    #热门page
    HR_8 = BASE_URL + '8hr/page/'
    #24小时
    HR_24 = BASE_URL + 'hot/page/'

HEADERS = {'User-Agent': USER_AGENT}

def soup_page_with_url(url):
    try:
        request = urllib2.Request(url, headers=HEADERS)
        res = urllib2.urlopen(request)
        page = res.read().decode('utf-8')
        soup = BeautifulSoup(page, 'lxml')
        return soup
    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print("连接失败:", e.reason)
            return None


class QBSpider(object):

    @staticmethod
    def get_page(page=1, page_type=Page_Type.HR_8):
        url = page_type + page
        soup_page = soup_page_with_url(url)
        return soup_page

    @staticmethod
    def get_users(page=1):
        '''

        Args:
            page: page index

        Returns: list of users

        '''
        soup_page = QBSpider.get_page(page=page)

    @staticmethod
    def get_articles_for_user(user):
        '''
        :type user:
        Args:
            user:

        Returns: articles of the user

        '''
        pass

    @staticmethod
    def get_comments_of_article(article):
        '''

        Args:
            article:

        Returns:comments of the article

        '''
        pass

    @staticmethod
    def save_pages():
        for i in range(MAX_PAGE):
            current_page = QBSpider.get_page(page=i)








