import time
import requests
import pandas as pd
import random

#定义睡眠时间
def sleep_time(time_sleep):
    sleep_time = random.randint(time_sleep,time_sleep+1) + random.random()*5
    time.sleep(sleep_time)

# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
def get_json_zhilian(kind, page=1,city='北京'):

    # 请求的url
    url = 'https://fe-api.zhaopin.com/c/i/sou?&pageSize=60&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.04693828&x-zp-page-request-id=faa64d9753f2402f98c2f2b741719edc-1544176723106-24778'
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
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
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
    print("正在爬取第"+str(page)+"页......")
    header = {
        'User-Agent': header}
    city_list = {
        '全国':'489',
        '北京':'530',
        '上海':'538',
        '深圳':'765',
        '广州':'763',
        '天津':'531',
        '武汉':'736',
        '成都':'801',
        '杭州':'653',
        '南京':'635',
        '青岛':'703',
        '大连':'600',
        '西安':'854',
        '厦门': '682',
        '长沙': '749',
        '苏州': '639',
        '济南': '702',
        '沈阳': '599',
        '郑州': '719',
        '哈尔滨': '622',
        '石家庄': '565',
        '太原': '576',
        '兰州': '864',
        '乌鲁木齐': '890',
        '西宁': '878',
        '拉萨': '847',
        '南宁': '785',
        '贵阳': '822',
        '福州': '681',
        '宁波': '654',
        '南昌': '691',
        '合肥': '664',
        '东莞': '779',
        '佛山': '768',
        '中山': '780',
        '珠海': '766',
        '海口': '799',
        '三亚': '800',
        '洛阳': '721',
        '保定': '570',
        '唐山': '566',
        '廊坊': '574',
        '无锡': '636',
        '常州': '638',
        '银川': '886',
        '呼和浩特': '587',
        '包头': '588',
        '烟台': '707',
        '潍坊': '708',
        '温州': '655',
    }
    param = {
        'start': (page-1)*60,
        'kw': kind,
        'cityId':city_list[city],
    }

    # 使用get()方法获取网页
    response = requests.get(url, headers=header,params=param)
    #response = requests.get(url,params=param)

    response.encoding = 'utf-8'
    #print(response.text)
    if response.status_code == 200:
        response = response.json()
        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        sleep_time(10)
        #print(response['data'])
        return response['data']
    return None


#接下来我们只需要每次翻页之后调用 get_json 获得请求的结果 再遍历取出需要的招聘信息即可


def crawler_zhilian(kind,city):

    print("*******************")
    Time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(Time)
    # 默认先查询第一页的数据
    #kind = 'python'
    # 请求一次 获取总条数
    position_result = get_json_zhilian(kind=kind,city=city)

    # 总条数
    total = position_result['numFound']
    print('智联招聘网{}职位，招聘信息总共{}条.....'.format(kind, total))
    # 每页15条 向上取整 算出总页数
    page_total = int(total/60)+1

    # 所有查询结果
    search_job_result = []
    for i in range(1, page_total + 1):
    # 为了节约效率 只爬去前100页的数据
    #for i in range(1,4):
        try:
            position_result = get_json_zhilian(kind=kind, page= i,city=city)
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            # 当前页的招聘信息
            page_python_job = []
            for j in position_result['results']:
                python_job = []
                # 公司全名
                python_job.append(j['company']['name'])
                # 公司规模
                python_job.append(j['company']['size']['name'])
                # 公司性质
                python_job.append(j['company']['type']['name'])
                #公司网址
                python_job.append(j['company']['url'])
                # 工作名称
                python_job.append(j['jobName'])
                # 工作链接
                python_job.append(j['positionURL'])
                # 招聘学历
                python_job.append(j['eduLevel']['name'])
                # 要求工作年限
                python_job.append(j['workingExp']['name'])
                # 薪资范围
                python_job.append(j['salary'])
                # 福利
                python_job.append(j['welfare'])
                # 招聘开始日期
                python_job.append(j['updateDate'])
                # 招聘更新日期
                python_job.append(j['createDate'])
                # 招聘截止日期
                python_job.append(j['endDate'])
                page_python_job.append(python_job)

            # 放入所有的列表中
            search_job_result += page_python_job
            print('智联招聘第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))

            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            time.sleep(20)
            # 将总数据转化为data frame再输出
            df = pd.DataFrame(data=page_python_job,
                              columns=['公司全名','公司规模','公司性质', '公司网址', '工作名称','工作链接', '招聘学历', '要求工作年限', '薪资范围', '福利','招聘开始日期','招聘更新日期','招聘截止日期'])
            df.to_csv(kind+'_zhilian_'+city+'_'+Time+'.csv', mode ='a',index=False, encoding='utf-8_sig')
        except Exception as e:
            print('Error', e)
            sleep_time(10)
    print("智联招聘网爬取完毕！")


