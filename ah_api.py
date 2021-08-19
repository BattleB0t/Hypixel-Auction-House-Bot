import requests
import eventlet
import json

##The additinal Data 
query_links = {
    "data":"https://api.hypixel.net/skyblock/auctions?key=APIKEY",
    "spesific_page":"https://api.hypixel.net/skyblock/auctions?key=APIKEY&page=PAGENUM"
}

#How long it takes for a http request to time out.
TimeOutInSeconds = 5

def format_query(query, auction_data_obj): #The auction_data_obj stores things like your API KEY and other data needed for querys.
    query = query_links[query]
    for key in auction_data_obj.additional_data:
        if key in query:
            query = query.replace(key, auction_data_obj.additional_data[key])

        else:
            print(f"query did not use {key}")

    print(query)
    return query


def request(query):
    try:
        with eventlet.Timeout(TimeOutInSeconds):
            return requests.get(query).json()
    except:
        return "FAILURE"


class auction_data:
    def __init__(self, addit_data):
        self.additional_data = addit_data
        self.data = {}

    def load_all_data(self): #This should only be done once a min.
        self.number_of_pages = request(format_query("data", self))["totalPages"]
        print(f"Loading {self.number_of_pages} Pages.")

        for page in range(self.number_of_pages):#range(number_of_pages):
            self.additional_data["PAGENUM"] = str(page)
            response = request(format_query("spesific_page", self))

            #If api request fails, it will re-try.
            if response == "FAILURE":
                print(f"Error Loading Page: {page}")
                print("Using previously loaded page data.")
                continue

            self.data[f"page{page}"] = response
            print(f"Loaded Page: {page}/{self.number_of_pages-1}")

