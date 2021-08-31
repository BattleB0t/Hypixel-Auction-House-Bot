#This is the random scripts that are used by the program.

"""
THINGS TO DO:
get a list of reforges.

"""

import os
import json
import threading
import pyperclip

import scripts.api_functions
import scripts.api

def list_to_string(list_data):
    lts = "".join(map(str,list_data))
    return lts

def remove_spaces(string):
    for space_count in range(string.count(" ")):
        string = string.replace(" ", "")
    return string


def request_all_pages():
    urls = scripts.api_functions.compile_all_urls()
    return scripts.api.many_requests(urls) #This contains a set, which contains all pages of the auction house


#THIS HAS NOT BEEN TESTED, THIS IS LIKELY FULL OF BUGS

def format_flip_data():
    formatted_data = {}
    for item_name in data_set:
        vals = scripts.functions.get_two_lowest_values(item_name)
        
        if len(vals) == 2:
            formatted_data[item_name] = {}
            formatted_data[item_name]["name"] = item_name #Idk why i put this here, i guess it could help me in the future ?????
            formatted_data[item_name]["lp"] = vals[0]
            formatted_data[item_name]["slp"] = vals[1]
            formatted_data[item_name]["margins"] = vals[1] - vals[0]

    return formatted_data

def get_two_lowest_values(item_name): #Item_name page is the str value of the item we want to call.
    keys = data_set[item_name].keys()
    keys = list(map(int, keys))
    return_values = {}

    for val_id in range(2):
        try:
            return_values[val_id] = min(keys)
        except:
            break #No more keys.
        
        try:
            keys.remove(min(keys))
        except:
            break #No more keys.

    return return_values
    

def find_smallest_value(data_set_page): #Data_set_page is the page of an entire item_name.
    lowest_value = min(data_set_page)
    return lowest_value

data_set = {}

def add_data_to_set(item_data):
    if item_data["item_name"] in data_set:
        data_set[item_data["item_name"]][item_data["starting_price"]] = item_data
    else:
        data_set[item_data["item_name"]] = {item_data["starting_price"]:item_data}




reforges = ["PLACEHOLDER"]

def scrape_item_data(item_str, bin_bool, uuid, starting_price):
    item_str = remove_spaces(item_str)
    #This is to stop bugs when formatting, removing spaces i found was the easiest way to fix some of my issues.

    remove_bins = True
    if bin_bool == False:
        if remove_bins == True:
            return

    present_reforge = ""
    present_stars = 0
    present_lvl = 0



    if any(reforge in item_str for reforge in reforges) == True:
        reforge_present = True
        
        for reforge in reforges:
            if reforge in item_str:
                present_reforge = reforge
                break



    if "✪" in item_str:
        present_stars = item_str.count("✪")
        item_str = item_str.replace("✪"*present_stars, "")
    
    if "[Lvl" in item_str:
        lvl_suffix_pointer = 3
        while lvl_suffix_pointer > 0:
            try:
                present_lvl = int(list_to_string(list(item_str)[4:4+lvl_suffix_pointer]))
                item_str = item_str.replace(f"[Lvl{present_lvl}]", "")
                break
            except:
                lvl_suffix_pointer -= 1

    
    add_data_to_set({"item_name":item_str, "reforge":present_reforge, "stars":present_stars, "lvl":present_lvl, "bin":bin_bool, "starting_price":starting_price, "auctionID":uuid}) #Lvl is only used by certain items and should be ignored most of the time.


def parse_all_page_data(all_page_data):

    for key in all_page_data:
        current_page = all_page_data[key]

        for auction in current_page["auctions"]:
            auc_bin = False
            try: #If an auction is not a bin it does not have the bin key.
                auc_bin = auction["bin"]
            except:
                pass
            
            threading.Thread(target=scrape_item_data, args=(auction["item_name"], auc_bin, auction["uuid"], auction["starting_bid"])).start()

def save_as_json(data, filepath, opentype="w"):
    json_object = json.dumps(data)

    with open(filepath, opentype) as file:
        file.write(json_object)

def read_from_json(filepath):
    with open(filepath, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

def load_to_clipboard(item_to_load):
    pyperclip.copy(item_to_load)

def file_search(file_path):
    return os.path.isfile(file_path)