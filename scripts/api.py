#This script contains all the api request code.
import requests
import asyncio

async def request(url):
    print(f"downloading: {url}")
    return requests.get(url).json()

def many_requests(urls): #URLs must be a list.
    responses = {}
    for url, url_num in urls, len(urls):
        responses[f"page{url_num}"] = asyncio.run(request(url))
    return responses
