import requests
from lxml import html

hh_headers = {'accept': '*/*',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
hh_url = 'https://hh.ru/search/vacancy?area=17&text=java'


def get_search_hh(headers, url):
    hh_sessions = requests.Session()
    request = hh_sessions.get(url, headers=headers)
    return_html = html.fromstring(request.text)
    return return_html


def get_jobs(headers, url):
    root = get_search_hh(headers, url)
    count_int = 1
    result_hh = []
    while True:
        count_jobs = str(count_int)
        result_hh2 = root.xpath(
            "//div[@class='vacancy-serp']//div[" + count_jobs + "]//div[1]//div[1]//div[1]//a[1]/text()")

        if result_hh2 == []:
            break
        result_hh.append(result_hh2)
        count_int += 1

    return result_hh


def record_to_file(files):
    with open("file22.txt", "w") as file:
        for i in files:
            file.write(str(i) + '\n')


get_jobs(hh_headers, hh_url)