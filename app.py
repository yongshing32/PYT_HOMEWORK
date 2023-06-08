from flask import Flask
import requests

app = Flask(__name__)
@app.route('/') # this is to route in your web extension
def welcome():
    # Welcome to the site homepage 
    guest_name = input('Please enter your name: ')
    return (greeting(guest_name))

def greeting(name):
    return f"{name}, welcome to the site"

def getdata():
    # retrieve data from API
    url = f"https://api.worldbank.org/v2/country"
    response = requests.get(url, {"format": "json", "per_page":"300"})
# check if request success
    if response.status_code == requests.codes.ok: 
        data = response.json()
        return (data)
    else: 
        return ("Please try again later")
 
# return the whole dataset
@app.route('/fulldata')
def api_data():
    return(getdata())

@app.route('/countrycapital')
def countryCapital():
    data = getdata()
    countryList = {}
    for country in data[1]:
        if country['capitalCity'] != "":
            countryList[country['name']] = country['capitalCity']
    return (countryList)

# return number of countries in each region
@app.route('/regions')
def regions():
    regionlist = {}
    data = getdata()
    for country in data[1]:
        if country['capitalCity'] != "":
            if country["region"]["value"] in regionlist: 
                regionlist[country["region"]["value"]] +=1
            else:
                regionlist[country['region']['value']] = 0
    return regionlist

# return list of countries for each regions
@app.route('/regions/countries')
def country_regions():
    country_region = {}
    data = getdata()
    for country in data[1]:
        if country['capitalCity'] != "":
            if country["region"]["value"] in country_region: 
                country_region[country["region"]["value"]].append(country['name'])
            else:
                country_region[country['region']['value']] = []
    return country_region

# return income groups
@app.route('/incomelevels')
def incomeLevel():
    incomegroups= {}
    data = getdata()
    for country in data[1]:
        if country['capitalCity'] != "":
            if country["incomeLevel"]["value"] in incomegroups: 
                incomegroups[country["incomeLevel"]["value"]] +=1
            elif country['incomeLevel']['value'] == "Not classified":
                    continue
            else:
                incomegroups[country['incomeLevel']['value']] = 0
    return incomegroups

# return countries for each income groups 
@app.route('/incomelevels/countries')
def country_incomelevel():
    country_incomelevel= {}
    data = getdata()
    for country in data[1]:
        if country['capitalCity'] != "":
            if country["incomeLevel"]["value"] in country_incomelevel: 
                country_incomelevel[country["incomeLevel"]["value"]].append(country['name'])
            else:
                country_incomelevel[country['incomeLevel']['value']] = []
    return country_incomelevel

#this is Flask framework that opens it in debugging mode. 
if __name__ == '__main__':
    app.run(debug=True)
