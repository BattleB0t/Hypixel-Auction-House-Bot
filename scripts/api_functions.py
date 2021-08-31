#Handles the api functions needed to manipulate that data.
import asyncio

import scripts.api

additional_data = {} #You're going to need to add an api key to this by using additional_data["APIKEY"] = "your api key"

#auction md collects the auction houses meta data.
def auction_md():
    data = asyncio.run(scripts.api.request("https://api.hypixel.net/skyblock/auctions"))
    return {"success":data["success"], "totalPages":data["totalPages"], "totalAuctions":data["totalAuctions"]}

#This formats the Urls by filling in placeholders with their real values.
def format_url(url):
    for key in additional_data:
        if key in url:
            url = url.replace(key, str(additional_data[key]))
    return url


#This will return the url for every page of the auction house
def compile_all_urls():
    urls = []
    auction_meta_data = auction_md()
    for page_num in range(auction_meta_data["totalPages"]):
        additional_data["PAGENUM"] = page_num
        urls.append(format_url("https://api.hypixel.net/skyblock/auctions?key=APIKEY&page=PAGENUM"))
    return urls