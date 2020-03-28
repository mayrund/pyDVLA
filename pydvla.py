###########################
# DVLA Vehicle MOT Status #
##########################

# Please install BeautifulSoup4 and Requests packages
from sys import argv
from bs4 import BeautifulSoup
import requests

formUrl = 'https://vehicleenquiry.service.gov.uk/ViewVehicle'

def getcar(manufacturer, licenseplate):
  resp = requests.post(formUrl, data = { 'Vrm': licenseplate, 'Make': manufacturer}, headers = {"Content-type": "application/x-www-form-urlencoded"} )
  html = resp.content
  soup = BeautifulSoup(html, 'html.parser')
  ul = soup.find('ul', {'class':"ul-data"}).find_all("li")
  for child in ul:
    span = child.find("span")
    strong = child.find("strong")
    print span.text + ": " + strong.text

if __name__ == '__main__':
    args = argv[1:]
    if len(args) is 2:
        print 'Downloading vehcile information from DVLA...\n'
        getcar(*args[:2])
    else:
        print "Usage: {0} manufacturer licenseplate".format(argv[0])
