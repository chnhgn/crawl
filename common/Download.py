import requests

class Download(object):
    
    def download(self, page_url):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(page_url, headers=user_agent)
        status_code = response.status_code
        
        if status_code == 200:
            return response.content
        else:
            return None