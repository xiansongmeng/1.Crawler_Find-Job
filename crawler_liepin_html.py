import time
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup
import re

#定义睡眠时间
def sleep_time(time_sleep):
    sleep_time = random.randint(time_sleep,time_sleep+1) + random.random()*5
    #print(sleep_time)
    time.sleep(sleep_time)

# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
def get_json_liepin(kind, page=1,city='北京'):

    print("正在爬取第" + str(page) + "页......")
    # 请求的url
    #url = 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new'
    url = 'https://www.liepin.com/zhaopin/?init=-1&headckid=9c8e662767a4ff16&fromSearchBtn=2&sfrom=click-pc_homepage-centre_searchbox-search_new&ckid=9c8e662767a4ff16&degradeFlag=0&siTag=I-7rQ0e90mv8a37po7dV3Q~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_unknown&d_ckId=06309a38f1bf466fd805183005b86898&d_curPage=0&d_pageSize=40&d_headId=06309a38f1bf466fd805183005b86898'
    # post请求参数

    # 更换header,可以参考http://www.useragentstring.com/pages/useragentstring.php
    headers = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'Mozilla/5.0 (Windows; U; Windows NT en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]
    header = random.choice(headers)
    #print(header)
    #print("#################")
    header = {
        'Host': 'www.liepin.com',
        'User-Agent': header}
    city_list = {
        '北京':'010',
        '上海':'020',
        '天津':'030',
        '广州':'050020',
        '深圳': '050090',
        '杭州': '070020',
        '武汉': '170020',
        '南京': '060020',
        '成都': '280020',
        '重庆': '040',
        '西安': '270020',
        '郑州': '150020',
        '青岛': '250070',
        '全国':'',
        '厦门': '090040',
        '长沙': '180020',
        '苏州': '060080',
        '济南': '250020',
        '沈阳': '210020',
        '哈尔滨': '160020',
        '石家庄': '140020',
        '太原': '260020',
        '兰州': '100020',
        '乌鲁木齐': '300020',
        '西宁': '240020',
        '拉萨': '290020',
        '南宁': '110020',
        '贵阳': '120020',
        '福州': '090020',
        '宁波': '070030',
        '南昌': '200020',
        '合肥': '080020',
        '东莞': '050040',
        '佛山': '050050',
        '中山': '050130',
        '珠海': '050140',
        '海口': '130020',
        '三亚': '130030',
        '洛阳': '150040',
        '保定': '140030',
        '唐山': '140080',
        '廊坊': '140060',
        '无锡': '060100',
        '常州': '060040',
        '银川': '230020',
        '呼和浩特': '220020',
        '包头': '220030',
        '烟台': '250120',
        '潍坊': '250110',
        '温州': '070040',

    }

    param = {
        'dqs':city_list[city],
        'key': kind,
        'curPage': page-1

    }

    response = requests.get(url, headers=header, params=param)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        #response = response.json()
        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        sleep_time(15)
        return response.text
    return None


#接下来我们只需要每次翻页之后调用 get_json 获得请求的结果 再遍历取出需要的招聘信息即可

#if __name__ == '__main__':
def crawler_liepin(kind,city):
    print("*******************")
    Time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(Time)
    # 默认先查询第一页的数据
    #kind = '用户研究'
    #city = '北京'
    #获取链接
    response = get_json_liepin(kind=kind, page=1, city=city)
    soup = BeautifulSoup(response, "html.parser")
    #print(soup.prettify())
    # 查看页数
    page_total_link = soup.find('a', class_='last').get('href').strip()  # 爬取每页中显示的最后一页URL信息
    page_total = int(re.findall('&curPage=(.*)', page_total_link)[-1])  # 从URL信息中提取最后一页页码
    print('猎聘网{}职位，在{}地区招聘信息总共{}条.....'.format(kind,city,page_total*40))

    search_job_result = []
    for i in range(1, page_total+1):
    # 为了节约效率 只爬去前100页的数据
    #for i in range(1,4):
        try:
            response = get_json_liepin(kind=kind, page=i, city=city)

            # 查找职位和公司总信息
            soup = BeautifulSoup(response, "html.parser")
            position_company = soup.find_all('div', class_='sojob-item-main clearfix')

            page_job = []

            for j in range(len(position_company)):
                try:
                    job = []
                    # 公司名称
                    job.append(position_company[j].find('p', class_='company-name').a.text.strip())
                    # 工作名称
                    job.append(position_company[j].find('div', class_='job-info').h3.get('title').strip())
                    #工作链接
                    if position_company[j].find('div', class_='job-info').h3.a.get('href').strip().find('https://www.liepin.com') >= 0:
                        job.append(position_company[j].find('div', class_='job-info').h3.a.get('href').strip())
                    else:
                        job.append('https://www.liepin.com' + position_company[j].find('div', class_='job-info').h3.a.get('href').strip())
                    # 总体要求
                    job.append(position_company[j].find('p', class_='condition clearfix').get('title').strip())
                    # 薪水待遇
                    job.append(position_company[j].find('span', class_='text-warning').text.strip())
                    # 工作地点
                    job.append(position_company[j].find(class_='area').text.strip()) #有些是a标签，有些事span标签，所以删掉
                    # 学历要求
                    job.append(position_company[j].find('span', class_='edu').text.strip())
                    # 工作年限要求
                    job.append(position_company[j].find('p', class_='condition clearfix').find_all('span')[-1].text.strip())  # 注意看，这个非常好
                    # 职位发布日期
                    job.append(position_company[j].find('p', class_='time-info clearfix').time.get('title').strip())
                    # 公司反馈时间
                    if position_company[j].find('p',class_='time-info clearfix').find('span') != None:
                        job.append(position_company[j].find('p', class_='time-info clearfix').span.text.strip())
                    else:
                        job.append('NA')

                    # 公司所处行业
                    job.append(position_company[j].find('p', class_='field-financing').text.strip())
                    # 公司福利
                    if position_company[j].find('p', class_='temptation clearfix') != None:
                        job.append(position_company[j].find('p', class_='temptation clearfix').text.strip())
                    else:
                        job.append('NA')
                    #print(job)
                    page_job.append(job)
                    #print(page_job)
                except Exception as e:
                    print('Error', e)
            # 放入所有的列表中
            search_job_result = search_job_result + page_job

            print('猎聘网第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            time.sleep(20)
            # 将总数据转化为data frame再输出
            df = pd.DataFrame(data = page_job,
                              columns=['公司名称','工作名称','工作链接','总体要求','薪水待遇','工作地点','学历要求','工作年限要求','职位发布日期','公司反馈时间','公司所处行业','公司福利'])
            df.to_csv(kind+'_liepin_'+city+'_'+Time+'.csv', mode ='a', index=False, encoding='utf-8_sig')

        except Exception as e:
            print('Error', e)
            sleep_time(10)
    print("猎聘网爬取完毕！")