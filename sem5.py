#5 Parsing
"""
Поиск pdf а сайте
"""
from urllib.request import urlopen

data = urlopen('http://artculturestudies.sias.ru/').read().decode('cp1251') #можно качать кусками с помощью read()
from html.parser import HTMLParser # круче супа т к ему похер на размер страницы т к не строит дерево у себя в памяти


def to_ref(string):
    return 'http://artculturestudies.sias.ru/' + string


def is_pdf(string):
    return '.pdf' in string

def checker_pdf(array):
    for item in array:
        if is_pdf(item):
            return item


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.href_array = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            a = dict(attrs).get('href') # берем по ключу
            if '.php' not in a and 'http' not in a and '.ru' not in a and '//' not in a and '#' not in a:
                self.href_array.append(to_ref(a))
    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


parser = MyHTMLParser()
parser.feed(data)
for ref in parser.href_array[:5]:
    data = urlopen(ref).read().decode('cp1251')
    new_parser = MyHTMLParser()
    parser.feed(data)
    print(new_parser.href_array)
