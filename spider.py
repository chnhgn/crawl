from common import URLManager
from common import Download
from common import DataOutput
from parsers import HtmlParser
import datetime


class SpiderMain(object):
    
    def __init__(self):
        self.manager = URLManager()
        self.down = Download()
        self.parser = HtmlParser()
        self.output = DataOutput()
    
    def crawl(self, root_url):
        content = self.down.download(root_url)
        movie_ids = self.parser.parse_urls(content)
        count = 0
        
        for mid in movie_ids:
            if count > 10:
                break
            movie_link = '''http://service.library.mtime.com/Movie.api?\
            Ajax_CallBack=true\
            &Ajax_CallBackType=Mtime.Library.Services\
            &Ajax_CallBackMethod=GetMovieOverviewRating\
            &Ajax_CrossDomain=1\
            &Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F{0}%2F\
            &t={1}\
            &Ajax_CallBackArgument0={2}\
            '''.format(mid, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"), mid)
            
            res = self.down.download(movie_link.replace(' ', ''))
            self.parser.parser_json(res)
            count += 1
        
        self.output.store_data(self.parser.items)
        self.output.close_connect()
        
        
        
if __name__ == '__main__':
    spider = SpiderMain()
    spider.crawl('http://theater.mtime.com/China_Beijing/')
    
    
    
    
    
    
    
    
    
    
    
    