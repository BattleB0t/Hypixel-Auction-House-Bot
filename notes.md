# Notes
It would appear that:
- The apikey isnt necissary for auction house API requests at this current time of: 21st August 2021
Additioanlly to this, if you do plan on using an API-KEY (if this is fixed in the future) you have to add the key to additional_data in api.py
by doing scrpts.api.additional_data["APIKEY"] = "your api key here"

