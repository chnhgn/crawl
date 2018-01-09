from common import Download
from parsers import HtmlParser

dl = Download()
parse = HtmlParser()

content = dl.download('http://theater.mtime.com/China_Beijing/')
res = parse._parse_movies(content)
print(res)