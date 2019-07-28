import requests
import re

html = '<p><b>Ко́фе</b> (от <a href="/wiki/%D0%90%D1%80%D0%B0%D0%B1%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA" title="Арабский язык">араб.</a>'
pp = r'(w[\w]+)(\/)(\S+\w)'
er = re.search(pp, html)
er = er.group()
wqw = requests.get(f'https://ru.wikipedia.org/wiki/{er}')
wqw.text
