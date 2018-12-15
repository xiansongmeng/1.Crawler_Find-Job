import time
import requests
import pandas as pd
import random


# 定义睡眠时间
def sleep_time(time_sleep):
    sleep_time = random.randint(time_sleep, time_sleep + 1) + random.random() * 10
    time.sleep(sleep_time)


# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
def get_json_lagou(kind, page=1, city='北京'):
    # 请求的url

    # post请求参数

    #更换header,可以参考http://www.useragentstring.com/pages/useragentstring.php
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
    print("正在爬取第" + str(page) + "页......")
    header = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': header}


    city_list = {
        '北京': '%E5%8C%97%E4%BA%AC',
        '上海': '%E4%B8%8A%E6%B5%B7',
        '深圳': '%E6%B7%B1%E5%9C%B3',
        '广州': '%E5%B9%BF%E5%B7%9E',
        '天津': '%E5%A4%A9%E6%B4%A5',
        '武汉': '%E6%AD%A6%E6%B1%89',
        '成都': '%E6%88%90%E9%83%BD',
        '杭州': '%E6%9D%AD%E5%B7%9E',
        '南京': '%E5%8D%97%E4%BA%AC',
        '青岛': '%E9%9D%92%E5%B2%9B',
        '大连': '%E5%A4%A7%E8%BF%9E',
        '西安': '%E8%A5%BF%E5%AE%89',
        '全国': '',
        '厦门': '%E5%8E%A6%E9%97%A8',
        '长沙': '',
        '苏州': '',
        '济南': '',
        '沈阳': '',
        '郑州': '',
        '哈尔滨': '',
        '石家庄': '',
        '太原': '',
        '兰州': '',
        '乌鲁木齐': '',
        '西宁': '',
        '拉萨': '',
        '南宁': '',
        '贵阳': '',
        '福州': '',
        '宁波': '',
        '南昌': '',
        '合肥': '',
        '东莞': '',
        '佛山': '',
        '中山': '',
        '珠海': '',
        '海口': '',
        '三亚': '',
        '洛阳': '',
        '保定': '',
        '唐山': '',
        '廊坊': '',
        '无锡': '',
        '常州': '',
        '银川': '',
        '呼和浩特': '',
        '包头': '',
        '烟台': '',
        '潍坊': '',
        '温州': '',
    }
    param = {
        # 'city': city_list[city],
        'pn': page,
        'kd': kind,

    }
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&city=' + city_list[city]
    # 使用get()方法获取网页
    response = requests.get(url, headers=header, params=param)
    '''
    #使用post()方法获取网页
    response = requests.post(url, headers=header, data=param)
    '''
    response.encoding = 'utf-8'
    #print(response.text)
    if response.status_code == 200:
        response = response.json()
        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        sleep_time(15)
        return response['content']['positionResult']
    return None


# 接下来我们只需要每次翻页之后调用 get_json 获得请求的结果 再遍历取出需要的招聘信息即可


def crawler_lagou(kind, city):
    print("*******************")
    Time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(Time)
    # 默认先查询第一页的数据
    # kind = 'python'
    # 请求一次 获取总条数
    position_result = get_json_lagou(kind=kind, city=city)

    # 总条数
    total = position_result['totalCount']
    print('拉钩网{}职位，招聘信息总共{}条.....'.format(kind, total))
    # 每页15条 向上取整 算出总页数
    # page_total = math.ceil(total/15)
    page_total = int(total / 15) + 1
    # 所有查询结果
    search_job_result = []
    for i in range(1, page_total+1):
    # 为了节约效率 只爬去前100页的数据
    #for i in range(1, 4):
        try:
            position_result = get_json_lagou(kind=kind, page=i, city=city)
            #print(position_result)
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            # 当前页的招聘信息
            page_python_job = []
            for j in position_result['result']:
                python_job = []
                # 公司全名
                python_job.append(j['companyFullName'])
                # 公司简称
                python_job.append(j['companyShortName'])
                # 公司规模
                python_job.append(j['companySize'])
                # 融资
                python_job.append(j['financeStage'])
                # 所属区域
                python_job.append(j['district'])
                # 职称
                python_job.append(j['positionName'])
                # 要求工作年限
                python_job.append(j['workYear'])
                # 招聘学历
                python_job.append(j['education'])
                # 薪资范围
                python_job.append(j['salary'])
                # 福利待遇
                python_job.append(j['positionAdvantage'])

                page_python_job.append(python_job)

            # 放入所有的列表中
            search_job_result += page_python_job
            print('拉勾网第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))
            # 每次抓取完成后,暂停一会,防止被服务器拉黑
            time.sleep(20)
            # 将总数据转化为data frame再输出
            #print(type(page_python_job))
            df = pd.DataFrame(data=page_python_job,
                              columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域', '职位名称', '工作经验', '学历要求', '工资', '职位福利'])
            df.to_csv(kind + '_lagou_'+city+'_'+ Time + '.csv', mode='a', index=False, encoding='utf-8_sig')
        except Exception as e:
            print('Error', e)
            sleep_time(10)
    print("拉钩网爬取完毕！")