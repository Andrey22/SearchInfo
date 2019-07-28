import requests
import re
import collections


def return_wikihtml(topic):
    wiki_req = requests.get(f'https://ru.wikipedia.org/wiki/{topic.capitalize()}')
    return wiki_req.text

def returns_words(topic):
    wiki_html = return_wikihtml(topic)
    wwords = re.findall('[а-яА-Я]{3,}', wiki_html)
    words_counter = collections.Counter()
    for word in wwords:
        words_counter[word] += 1
    return words_counter.most_common(10)

print(returns_words('кофе'))


import requests_html