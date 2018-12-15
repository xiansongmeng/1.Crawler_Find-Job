import time
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup
import re


#定义睡眠时间
def sleep_time(time_sleep):
    sleep_time = random.randint(time_sleep,time_sleep+1) + random.random()*10
    #print(sleep_time)
    time.sleep(sleep_time)

# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
def get_json_51job(kind, page=1,city='北京'):

    print("正在爬取第" + str(page) + "页......")

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
    header = {
        'Host': 'search.51job.com',
        'User-Agent': header}
    city_list = {
        '北京':'010000',
        '上海':'020000',
        '天津':'050000',
        '广州':'030200',
        '深圳': '040000',
        '杭州': '080200',
        '武汉': '180200',
        '南京': '070200',
        '成都': '090200',
        '重庆': '060000',
        '西安': '200200',
        '郑州': '170200',
        '青岛': '120300',
        '全国': '000000',
        '厦门': '110300',
        '长沙': '190200',
        '苏州': '070300',
        '济南': '120200',
        '沈阳': '230200',
        '哈尔滨': '220200',
        '石家庄': '160200',
        '太原': '210200',
        '兰州': '270200',
        '乌鲁木齐': '310200',
        '西宁': '320200',
        '拉萨': '300200',
        '南宁': '140200',
        '贵阳': '260200',
        '福州': '110200',
        '宁波': '080300',
        '南昌': '130200',
        '合肥': '150200',
        '东莞': '030800',
        '佛山': '030600',
        '中山': '030700',
        '珠海': '030500',
        '海口': '100200',
        '三亚': '100300',
        '洛阳': '170300',
        '保定': '160400',
        '唐山': '160500',
        '廊坊': '160300',
        '无锡': '070400',
        '常州': '070500',
        '银川': '290200',
        '呼和浩特': '280200',
        '包头': '280400',
        '烟台': '120400',
        '潍坊': '120500',
        '温州': '080400',
    }

    # 请求的url
    url = 'https://search.51job.com/list/' + city_list[city] + ',000000,0000,00,9,99,' + kind + ',2,' + str(page) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    response = requests.get(url, headers=header)
    html_text = response.text.encode('ISO-8859-1', 'ignore').decode('gbk', 'ignore')   #ISO-8859-1是request显示的编码，gbk是网页显示的编码

    if response.status_code == 200:

        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        sleep_time(10)
        return html_text
    return None


#接下来我们只需要每次翻页之后调用 get_json 获得请求的结果 再遍历取出需要的招聘信息即可

#if __name__ == '__main__':
def crawler_51job(kind,city):
    print("*******************")
    Time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(Time)
    # 默认先查询第一页的数据
    #kind = '用户研究'
    #city = '北京'
    #获取链接
    response = get_json_51job(kind=kind, page=1, city=city)
    soup = BeautifulSoup(response, "html.parser")
    #print(soup.prettify())

    # 查看页数
    page_total = soup.find('span', class_="td").text.strip()
    page = int(re.findall('共(.*)页',page_total)[0])

    #查看工作条数
    total_numb = soup.find('div', class_="rt").text.strip()
    total = int(re.findall('共(.*)条',total_numb)[0])
    print('51job网{}职位，在{}地区招聘信息总共{}条.....'.format(kind,city,total))

    search_job_result = []
    for i in range(1,page+1):
    # 为了节约效率 只爬去前100页的数据
    #for i in range(1,4):
        try:
            response = get_json_51job(kind=kind, page=i, city=city)

            # 查找职位和公司总信息
            soup = BeautifulSoup(response, "html.parser")
            position_company = soup.find('div', id='resultList', class_='dw_table').find_all('div', class_='el')[1:]
            #print(position_company)
            page_job = []

            for j in range(len(position_company)):
                try:
                    job = []
                    # 公司名称
                    job.append(position_company[j].find('span', class_='t2').a.text.strip())

                    #公司网页
                    job.append(position_company[j].find('span', class_='t2').a.get('href').strip())

                    # 工作名称
                    job.append(position_company[j].find('p', class_='t1').find('a').text.strip())

                    #工作链接
                    job.append(position_company[j].find('p', class_='t1').find('a').get('href').strip())

                    # 薪水待遇
                    job.append(position_company[j].find('span', class_='t4').text.strip())

                    # 工作地点
                    job.append(position_company[j].find('span', class_='t3').text.strip())

                    # 职位发布日期
                    job.append(position_company[j].find('span', class_='t5').text.strip())

                    #print(job)
                    page_job.append(job)

                except Exception as e:
                    print('Error', e)
            # 放入所有的列表中
            search_job_result = search_job_result + page_job

            print('51job网第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            time.sleep(15)
            # 将总数据转化为data frame再输出
            df = pd.DataFrame(data = page_job,
                              columns=['公司名称','公司网页','工作名称','工作链接','薪水待遇','工作地点','职位发布日期'])
            df.to_csv(kind+'_51Job_'+city+'_'+Time+'.csv', mode ='a', index=False, encoding='utf-8_sig')

        except Exception as e:
            print('Error', e)
            sleep_time(10)
    print("前程无忧网爬取完毕！")