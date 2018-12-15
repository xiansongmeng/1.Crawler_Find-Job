import time
import requests
import pandas as pd
import random
from math import ceil
from bs4 import BeautifulSoup


#定义睡眠时间
def sleep_time(time_sleep):
    sleep_time = random.randint(time_sleep,time_sleep+1) + random.random()*5
    #print(sleep_time)
    time.sleep(sleep_time)

# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
def get_json_ChinaHR(kind, page=1,city='北京'):

    print("正在爬取第" + str(page) + "页......")


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
        'Host': 'search.chinahr.com',
        'User-Agent': header}
    city_list = {
        '北京':'bj',
        '上海':'sh',
        '天津':'tj',
        '广州':'gz',
        '深圳': 'sz',
        '杭州': 'hz',
        '武汉': 'wh',
        '南京': 'nj',
        '成都': 'cd',
        '重庆': 'cq',
        '西安': 'xa',
        '郑州': 'zz',
        '青岛': 'qd',
        '全国': 'bj', #中华英才网没有全国的信息
        '厦门': 'xm',
        '长沙': 'cs',
        '苏州': 'sz',
        '济南': 'jn',
        '沈阳': 'sy',
        '哈尔滨': 'hrb',
        '石家庄': 'sjz',
        '太原': 'ty',
        '兰州': 'lz',
        '乌鲁木齐': 'xj',
        '西宁': 'xn',
        '拉萨': 'lasa',
        '南宁': 'nn',
        '贵阳': 'gy',
        '福州': 'fz',
        '宁波': 'nb',
        '南昌': 'nc',
        '合肥': 'hf',
        '东莞': 'dg',
        '佛山': 'fs',
        '中山': 'zs',
        '珠海': 'zh',
        '海口': 'haikou',
        '三亚': 'sanya',
        '洛阳': 'luoyang',
        '保定': 'bd',
        '唐山': 'ts',
        '廊坊': 'lf',
        '无锡': 'wx',
        '常州': 'cz',
        '银川': 'yinchuan',
        '呼和浩特': 'hu',
        '包头': 'bt',
        '烟台': 'yt',
        '潍坊': 'wf',
        '温州': 'wz',
    }

    # 请求的url
    url = 'http://search.chinahr.com/'+city_list[city]+'/job/pn'+str(page)+'/?key='+kind
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        #response = response.json()
        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        sleep_time(15)
        return response.text
    return None


#接下来我们只需要每次翻页之后调用 get_json 获得请求的结果 再遍历取出需要的招聘信息即可

#if __name__ == '__main__':
def crawler_ChinaHR(kind,city):
    print("*******************")
    Time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(Time)
    # 默认先查询第一页的数据
    #kind = '用户研究'
    #city = '北京'
    #获取链接
    response = get_json_ChinaHR(kind=kind, page=1, city=city)
    soup = BeautifulSoup(response, "html.parser")
    #print(soup.prettify())

    # 查看页数
    total = int(soup.find('p', class_='total-jobs').span.text.strip())
    page = ceil(total/30)
    print('中华英才网{}职位，在{}地区招聘信息总共{}条.....'.format(kind,city,total))

    search_job_result = []
    for i in range(1,page+1):
    # 为了节约效率 只爬去前100页的数据
    #for i in range(1,4):
        try:
            response = get_json_ChinaHR(kind=kind, page=i, city=city)

            # 查找职位和公司总信息
            soup = BeautifulSoup(response, "html.parser")
            position_company = soup.find('div', class_='job-list-box').find_all('div', class_='jobList pc_search_listclick')

            page_job = []

            for j in range(len(position_company)):
                try:
                    job = []
                    #print(position_company[j])
                    # 公司名称
                    job.append(position_company[j].find('li', class_='job-company').text.strip())
                    #print(job)
                    #招聘信息来源
                    if position_company[j].find('li', class_='fabu-date').find('span') != None:
                        job.append(position_company[j].find('li', class_='fabu-date').find('span').text.strip())
                    else:
                        job.append('NA')
                    #print(job)
                    # 工作名称
                    job.append(position_company[j].find('li', class_='job-name').text.strip())
                    #print(job)
                    #工作链接
                    job.append(position_company[j].get('data-detail').strip())
                    #print(job)
                    # 薪水待遇
                    job.append(position_company[j].find('li', class_='job-salary').text.strip())
                    #print(job)
                    # 工作地点
                    job.append(position_company[j].find('li', class_='job-address').text.strip()) #有些是a标签，有些事span标签，所以删掉
                    #print(job)
                    # 学历要求
                    job.append(position_company[j].find('li', class_='job-address').text.strip()) #与工作地点的类似
                    #print(job)
                    # 工作年限要求
                    job.append(position_company[j].find('li', class_='job-address').text.strip()) #与工作地点的类似
                    #print(job)
                    # 职位发布日期
                    job.append(position_company[j].find('li', class_='fabu-date').text.strip())
                    #print(job)
                    # 公司所处行业
                    job.append(position_company[j].find('li', class_='job-address').span.text.strip())
                    #print(job)
                    # 公司福利
                    job.append(position_company[j].find('div', class_='job_wel clearfix').text.strip())
                    #print(job)
                    # 岗位职责
                    job.append(position_company[j].find('p', class_='l3').text.strip())

                    #print(job)
                    page_job.append(job)
                    #print(page_job)
                except Exception as e:
                    print('Error', e)
            # 放入所有的列表中
            search_job_result = search_job_result + page_job

            print('中华英才网第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            time.sleep(20)
            # 将总数据转化为data frame再输出
            df = pd.DataFrame(data = page_job,
                              columns=['公司名称','招聘信息来源','工作名称','工作链接','薪水待遇','工作地点','学历要求','工作年限要求','职位发布日期','公司所处行业','公司福利','岗位职责'])
            df.to_csv(kind+'_ChinaHR_'+city+'_'+Time+'.csv', mode ='a', index=False, encoding='utf-8_sig')

        except Exception as e:
            print('Error', e)
            sleep_time(10)
    print("中华英才网爬取完毕！")