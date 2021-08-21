#This is the random scripts that are used by the program.
import scripts.api_functions
import scripts.api

def request_all_pages():
    urls = scripts.api_functions.compile_all_urls()
    return scripts.api.many_requests(urls) #This contains a set, which contains all pages of the auction house
