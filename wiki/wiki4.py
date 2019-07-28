import requests
import re
import collections


def return_wikihtml(topic):
    wiki_req = requests.get(f'https://ru.wikipedia.org/wiki/{topic.capitalize()}')
    return wiki_req.text


def returns_words(topic):
    wwords = re.findall('[а-яА-Я]{3,}', topic)
    words_counter = collections.Counter()
    for word in wwords:
        words_counter[word] += 1
    return words_counter.items()


def search_first_link(topic):
    html = return_wikihtml(topic)
    copy_2_link = r'(id\=\"Ссылки)([\W\w]+)'
    copy_link = r'https\:\/\/([a-zA-Z]+.\w+\/\w+)+(\w)|http\:\/\/([a-zA-Z]+.\w+.\w+)+(\w)+'
    link_found = re.search(copy_2_link, html)
    link_found = link_found.group()
    link_wiki = re.search(copy_link, link_found)
    link_wiki = link_wiki.group()
    new_html = requests.get(f'{link_wiki}')
    new_html = new_html.text
    new_html_to_file = returns_words(new_html)
    return record_file(new_html_to_file)


def record_file(files):
    with open("file223.txt", "w") as file:
        for i in files:
            file.write(str(i) + '\n')


def search_all_link(topic):
    html = return_wikihtml(topic)
    hyperlink_patern = r'\<a href'
    copy_2_link = r'(id\=\"Ссылки)([\W\w]+)'
    copy_link = r'https\:\/\/([a-zA-Z]+.\w+\/\w+)+(\w)|http\:\/\/([a-zA-Z]+.\w+.\w+)+(\w)+'
    link_found = re.search(copy_2_link, html)
    link_found = link_found.group()
    link_wiki = re.search(copy_link, link_found)
    link_wiki = link_wiki.group()
    count_link = 0
    for i in link_found:
        if i == hyperlink_patern:
            count_link += 1
    return count_link

search_all_link('Кофе')



#search_first_link('Кофе')