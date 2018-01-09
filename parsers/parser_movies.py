import re

class HtmlParser(object):
    
    def parser_urls(self, html_content):
        pass
    
    def _parse_movies(self, html_content):
        pattern = re.compile(r'http://movie.mtime.com/(\d+)/')
        match = pattern.findall(r'%s' % html_content)
        return set(match)