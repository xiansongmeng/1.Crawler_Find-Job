import crawler_lagou_json
import crawler_zhilian_json
import crawler_liepin_html
import crawler_Boss_html
import crawler_51job_html
import crawler_ChinaHR_html
import sys

if __name__ == '__main__':
    print("*******************************************")
    print("Version 0.1 技术问题请联系QQ&微信:1047254058")
    print("*******************************************")
    print("请输入您要查找的工作岗位名称")
    kind = input("请在此输入:")
    print("################################")
    print("请输入您要查找工作的城市(例如：全国，北京，上海，广州，深圳，天津，杭州等)")
    city = input("请在此输入:")

    try:
        crawler_zhilian_json.crawler_zhilian(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    try:
        crawler_liepin_html.crawler_liepin(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    try:
        crawler_Boss_html.crawler_zhipin(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    try:
        crawler_51job_html.crawler_51job(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    try:
        crawler_lagou_json.crawler_lagou(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    try:
        crawler_ChinaHR_html.crawler_ChinaHR(kind=kind, city=city)
    except Exception as e:
        print('Error', e)

    sys.exit()