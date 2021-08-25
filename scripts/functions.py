#This is the random scripts that are used by the program.

import json

import scripts.api_functions
import scripts.api

def request_all_pages():
    urls = scripts.api_functions.compile_all_urls()
    return scripts.api.many_requests(urls) #This contains a set, which contains all pages of the auction house


""" #THIS IS STILL BEING DEVELOPED#
def parse_all_page_data(all_page_data):


    for key in all_page_data:
        current_page = all_page_data[key]

        for auction in current_page["auctions"]:

            current_auction = current_page["auctions"][auction]
"""


def save_as_json(data, filepath, opentype="w"):
    json_object = json.dumps(data)

    with open(filepath, opentype) as file:
        file.write(json_object)

def read_from_json(filepath):
    with open(filepath, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object
