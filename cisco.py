import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass
from pprint import pprint

user = input("Enter you Username: ")
password = getpass("Enter your Password: ")

BASIC = 'https://sandboxdnac.cisco.com'
authApi = "/dna/system/api/v1/auth/token"
deviceApi = "/dna/intent/api/v1/network-device"

authPayLoad={}
authHeaders = {'Content-Type': 'application/json',
'Accept': 'application/json'}
dnaAuth = BASIC + authApi

aResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(user, password), headers=authHeaders, data=authPayLoad)

tokenJSON = aResponse.json()

TOKEN = tokenJSON['Token']

devices = BASIC + deviceApi




getPayload={}
getHeader= {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': TOKEN
}

getResponse = requests.get(devices, headers=getHeader, data=getPayload)

getJson = getResponse.json()

pprint(getJson)
