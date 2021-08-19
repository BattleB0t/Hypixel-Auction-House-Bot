import ah_api
from pprint import pprint

api_key=""

ah_instance = ah_api.auction_data({"APIKEY":api_key})
ah_instance.load_all_data()


while True:
    try:
        pprint(ah_instance.data[input("Name The Page You Want To View: ")])
    except:
        print("Page Not Found")
