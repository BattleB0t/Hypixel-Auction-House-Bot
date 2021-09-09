#This script contains all the api request code.
from typing import final
import requests
import threading

final_page_Value = 0
all_pages_downloaded = False

def request(url):
    print(f"Requesting: {url}")
    return requests.get(url, timeout=10).json()


def many_requests(urls): #URLs must be a list.
    global responses
    Final_Page_Value = len(urls)-1
    responses = {}
    page_incrimentor = 0
    for url in urls:
        responses[f"page{page_incrimentor}"] = request(url)
        page_incrimentor += 1
    return responses
