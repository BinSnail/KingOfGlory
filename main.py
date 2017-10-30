# _*_ coding:utf-8 _*_
import requests
import re
import os

# 导入Json文件 （里面有所有英雄的名字以及数字）
url = 'https://pvp.qq.com/web201605/js/herolist.json'  # 英雄的名字json
head = {'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
html = requests.get(url, headers=head)
html = requests.get(url)
html_json = html.json()

# 提取英雄名字和数字

hero_name = list(map(lambda x: x['cname'], html_json))  # 名字
hero_number = list(map(lambda x: x['ename'], html_json))  # 数字


def main():  # 用于下载并保存图片

    ii = 0
    for v in hero_number:
        print(hero_name[ii])
    os.mkdir("C:/Users/Administrator/Desktop/python/wangzherongyao/home/" + hero_name[ii])
    os.chdir("C:/Users/Administrator/Desktop/python/wangzherongyao/home/" + hero_name[ii])
    ii = ii + 1
    for u in range(12):
        onehero_links = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/' + str(v) + '/' + str(
            v) + '-mobileskin-' + str(u) + '.jpg'
        im = requests.get(onehero_links)
        if im.status_code == 200:
            iv = re.split('-', onehero_links)
            open(iv[-1], 'wb').write(im.content)


main()
