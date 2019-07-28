import requests
from lxml import html
import pprint
import re

vacancy_input = input('Please enter the name of the vacancy: ')
number_of_pages = int(input('Please enter the count of pages: '))


def get_search_hh(headers, url):
    hh_sessions = requests.Session()
    request = hh_sessions.get(url, headers=headers)
    return_html = html.fromstring(request.text)
    return return_html


def clear_texts(text):  # функция для очистки от не лишних символов
    text = str(text)
    text2 = text.replace("]", '')
    text3 = text2.replace("'", "")
    text4 = text3.replace("[", '')
    text5 = text4.replace("]", '')
    text6 = text5.replace("\\", '')
    text7 = text6.replace("xa0", ' ')
    return text7


def record_to_file(files, name_file):  # функция для записи в файл с именем введенный в number_of_pages
    with open(f"{name_file}.csv", "w") as file:
        file.write(''.join(files))


def get_jobs(root):  # функция для парсинга одной станицы
    count_int = 1
    result_str = ''
    while True:
        count_jobs = str(count_int)
        result_hh_salary = root.xpath(
            "/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[" + count_jobs + "]/div[1]/div[2]/div[1]/text()")
        if result_hh_salary == []:
            result_hh_salary = 'Не указанна'
        result_hh_salary = clear_texts(result_hh_salary)
        result_hh_name = root.xpath(
            "//div[@class='vacancy-serp']//div[" + count_jobs + "]//div[1]//div[1]//div[1]//a[1]/text()")
        result_hh_name = clear_texts(result_hh_name)
        count_int += 1
        empty_7, empty_8, empty_15, empty_16 = '7', '8', '15', '16'
        if count_jobs == empty_7:
            continue
        if count_jobs == empty_8:
            continue
        if count_jobs == empty_15:
            continue
        if count_jobs == empty_16:
            continue
        result_hh_link = root.xpath("//div[@class='vacancy-serp']//div[2]//div[1]//div[1]//div[1]//a[1]/@href")
        result_hh_link = clear_texts(result_hh_link)
        if count_int == 26:
            break
        result_str += f'Вакансия {str(result_hh_name)} - Зарплата {str(result_hh_salary)} - Link {str(result_hh_link)} \n'

    return result_str


def get_all_vacancy(vacancy,
                    page_numbers):  # функция для парсинга более одной страницы. vacancy - необходимо ввести название вакансии, page_numbers - ввести кол-во страниц для парсинга
    hh_headers = {'accept': '*/*',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    count_pages = 0
    all_pages = []
    while True:
        hh_url = (f"https://hh.ru/search/vacancy?area=1&text={vacancy}&page={count_pages}")

        hh_one_root_page = get_search_hh(hh_headers, hh_url)
        jobs_one_page = get_jobs(hh_one_root_page)
        if count_pages == page_numbers:
            break
        count_pages += 1
        all_pages.append(jobs_one_page)


    return record_to_file(all_pages, vacancy)


get_all_vacancy(vacancy_input, number_of_pages)