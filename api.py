"""
Simply put, your main objective for this coding challenge is to send an API request to a server, get the data, then build a solution after getting the data.

For each partner, you need to categorize them according to the country in which they must attend the meeting. Find a way to determine which availability dates work best for everyone in EACH country. If a date doesn't work for a specific partner, they simply will not be able to attend the meeting.
The kicker: this meeting will last a total of two days. Because of this, you must find a RANGE of two dates that work best for everyone. For whichever two days work the best, only display the first date everyone can start.
When you've finished, send a POST request to the same API (Google how to do this!!!). You MUST send the data back to the server in the form a DICTIONARY with a key of 'data'. Otherwise you will get an error. Once you make the request, look through some of the requests object's attributes to see if you get a server response code of 200. If you do, you were successful in building your solution. Otherwise, hit the drawing board and try again!
"""

'https://ct-mock-tech-assessment.herokuapp.com/'


#Current Version: This version will pull data from the ct-mock-tech-assessment url. Pull_data_dict function works perfectly so far. find_available_dates needs to be fixed.

import urllib.request
import json


#def functions
def url_request(url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent', "Brandon")
    data = urllib.request.urlopen(request).read()
    parsed_data = json.loads(data)
    return parsed_data


def pull_partners_dict():
    country_dict = {

    }
    partners_response = url_request('https://ct-mock-tech-assessment.herokuapp.com/')
    for partner_dict in partners_response["partners"]:
        partner = Partner(partner_dict["firstName"], partner_dict["lastName"], partner_dict["email"],
                          partner_dict["country"], partner_dict["availableDates"])
        partner_country = partner_dict["country"]
        if partner_country in country_dict:
            country_dict[partner_country].append(partner)
        else:
            country_dict[partner_country] = [partner]
    return country_dict
    # the returned value from this function will be a parameter for find_available_dates

def find_available_dates(partners):
    dates_dict = {
    }
    for partner in partners:
        for date in partner.dates_available:
            if date in dates_dict:
                dates_dict[date].append(partner)
            else:
                dates_dict[date].append(partner)
    pass

#def classes
class Partner():
    def __init__(self, first_name, last_name, email, country, dates_available):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.dates_available = dates_available

    def __repr__(self):
        return self.email
        # makes finding individuals in the "variable" debugger tab easier,

#call functions
pull_partners_list()
find_available_dates()