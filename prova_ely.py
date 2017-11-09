from bs4 import BeautifulSoup
import re
import requests

def main(*args, **kwargs):
	search_links('href','http://example.webscraping.com/',1)

def search(keyword, url, deth):
    response = requests.get(url)
    html_sem_tags = BeautifulSoup(response.text, 'html.parser')
    index = html_sem_tags.text.find(keyword)
    print(html_sem_tags.text[index-10:index+10],"\n"+response.url)

def search_links(keyword, url, deth):
    response = requests.get(url)
    m = re.search(r"((http[s]):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?", response.text)
    print(m.group(0))
    

    
if __name__ == '__main__':
	main()
