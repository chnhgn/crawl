#-*-  coding:utf-8 -*-
import requests

class Download(object):
    
    def download(self, page_url):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(page_url, headers=user_agent)
        status_code = response.status_code
        
        if status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None