#This script contains all the api request code.
import requests
import asyncio

async def request(url):
    print(f"downloading: {url}")
    return requests.get(url).json()

def many_requests(urls): #URLs must be a list.
    responses = {}
    page_incrimentor = 0
    for url in urls:
        responses[f"page{page_incrimentor}"] = asyncio.run(request(url))
        page_incrimentor += 1
    return responses
