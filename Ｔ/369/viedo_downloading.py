










# 查询的方法
import urllib.request

import pymysql
import requests
from lxml import etree
# from selenium import webdriver
#
# driver = webdriver.Chrome()

def get_first_page(url):
    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    # time.sleep(3)
    return html

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

def call_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None





def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='FUNS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,600):
        sql = 'select link from viedos where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['link']
        url = Num
        yield url





def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    selector = etree.HTML(html)
    link = selector.xpath("//div[@class='image-holder']/video/@src")
    for link_single in link:
        urllib.request.urlretrieve(link_single, '/home/gb/viedos/%s.mp4' % link_single[-10:-1])



if __name__ =='__main__':
    for url_str in Python_sel_Mysql():
        print(url_str)
        html = call_page(url_str)
        parse_html(html)
