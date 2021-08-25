#This is the random scripts that are used by the program.

import json

import scripts.api_functions
import scripts.api

def request_all_pages():
    urls = scripts.api_functions.compile_all_urls()
    return scripts.api.many_requests(urls) #This contains a set, which contains all pages of the auction house


#THIS HAS NOT BEEN TESTED, THIS IS LIKELY FULL OF BUGS
def parse_all_page_data(all_page_data):
    parsed_data = {}

    for key in all_page_data:
        print(key)
        current_page = all_page_data[key]

        for auction in current_page["auctions"]:
            #{"tier":auction["tier"], "starting_price":auction["starting_bid"], "bin":auction["bin"], "uuid":auction["uuid"], "auctioneer":auction["auctioneer"]}
            
            if auction["item_name"] in parsed_data:
                auction["item_name"].append({"tier":auction["tier"], "starting_price":auction["starting_bid"], "bin":auction["bin"], "uuid":auction["uuid"], "auctioneer":auction["auctioneer"]})

            else:
                auction["item_name"] = []
                auction["item_name"].append({"tier":auction["tier"], "starting_price":auction["starting_bid"], "bin":auction["bin"], "uuid":auction["uuid"], "auctioneer":auction["auctioneer"]})
            



def save_as_json(data, filepath, opentype="w"):
    json_object = json.dumps(data)

    with open(filepath, opentype) as file:
        file.write(json_object)

def read_from_json(filepath):
    with open(filepath, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object
