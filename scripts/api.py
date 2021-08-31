#This script contains all the api request code.
import requests
import threading


def request(url):
    print(f"downloading: {url}")
    return requests.get(url).json()

def request_and_page(url, page_incrimentor):
    responses[f"page{page_incrimentor}"] = request(url)

def many_requests(urls): #URLs must be a list.
    global responses
    responses = {}    
    page_incrimentor = 0
    for url in urls:
        threading.Thread(target=request_and_page, args=(url, page_incrimentor)).start()
        page_incrimentor += 1
    return responses