import requests_html
import requests
from requests_html import HTMLSession


origin = "amst"
#input("Enter city of Origin: ")
destination = "pari"
url = "https://www.skyscanner.co.il/transport/flights/"+ origin+"/"+ destination +"/210918/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27539733&inboundaltsenabled=false&infants=0&originentityid=27546296&outboundaltsenabled=false&preferdirects=false&preferflexible=false&ref=home&rtn=0"
   
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)