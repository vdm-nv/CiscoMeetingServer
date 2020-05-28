# CiscoMeetingServer
use Python and API for CMS

in script you need to insert:

URL = 'https://{IP_CMS}:{PORT}/api/v1/coSpaces/' where :
  - {IP_CMS} - ip address of your Cisco Meeting Server
  - {PORT} - TCP port

headers = {
  'Authorization': 'Basic {Get Password from Postman app}'
}
  - {Get Password from Postman app} copy from Postman app

## Requirements:
 - python 3
 - pip
 - requests
 - xmltodict

## Installation:
	pip install requests
 	pip install xmltodict
