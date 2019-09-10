import requests

import json

import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) '
    'AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'referer': 'https://m.lagou.com/search.html'

}


def get_cookies():
    url = 'https://m.lagou.com/search.html'
    return requests.get(url, headers=headers).cookies


def get_page_data(url, cookies):
    resp = requests.get(url, headers=headers, cookies=cookies)
    for i in json.loads(resp.content.decode('utf-8'))['content']['data']['page']['result']:
<<<<<<< HEAD
        print(i)


def main():
    cookies = get_cookies()
    end_page = 0
    for i in range(1, sys.maxsize, 1):
        url = 'https://m.lagou.com/search.json?city=上海&positionName=python&pageNo=%s&pageSize=15' % i
        if i % 10 == 0:
            cookies = get_cookies()
        try:
            get_page_data(url, cookies)
=======
        # print(i)
        yield i


def parse_data(i):
    # for i in user_list:
    #     print(i)
    company = i['companyFullName']
    link = str(i['positionId'])
    complete_link = 'https://www.lagou.com/jobs/' + link + '.html'
    time = i['createTime']
    salary = i['salary']
    company_info = i['companyId']
    complete_company_info = 'https://www.lagou.com/gongsi/' + str(company_info) + '.html'
    # link = 'https://www.lagou.com/jobs/' + i['positionId'] + '.html'
    print({
        '公司': company,
        '发布时间': time,
        '工资': salary,
        '链接': complete_link,
        '公司链接': complete_company_info
    })
    # print(company, complete_link)


def main(city, keyword):
    cookies = get_cookies()
    end_page = 0
    for i in range(1, sys.maxsize, 1):
        url = 'https://m.lagou.com/search.json?city=%s&positionName=%s&pageNo=%s&pageSize=15' % (city, keyword, i)
        if i % 10 == 0:
            cookies = get_cookies()
        try:
            for data in get_page_data(url, cookies):
                # print('111')
                parse_data(data)
>>>>>>> add search function
        except KeyError as e:
            end_page += 1
            if end_page >= 3:
                break


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    city = input('please input you city:>>').strip()
    keyword = input('please input you choice:>>').strip()
    main(city, keyword)
>>>>>>> add search function
