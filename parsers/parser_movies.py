import re
import json
import sys


class HtmlParser(object):
    
    def __init__(self):
        self.items = []
    
    def parser_json(self, response):
        data = {}
        pattern = re.compile(r'=(.*?);')
        match = pattern.findall(response)
        content = json.loads(match[0])
        
        data['movieId'] = content['value']['movieRating']['MovieId']
        data['isRelease'] = content['value']['isRelease']
        data['movieTitle'] = content['value']['movieTitle']
        data['RatingFinal'] = content['value']['movieRating']['RatingFinal']
        
        print('adding an item...')     
        self.items.append(tuple(data.values()))
    
    def parse_urls(self, html_content):
        pattern = re.compile(r'http://movie.mtime.com/(\d+)/')
        match = pattern.findall(r'%s' % html_content)
        return list(set(match))
    
    
    
    
    