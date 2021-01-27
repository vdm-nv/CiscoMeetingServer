# CiscoMeetingServer
use Python and API for CMS

In script you need to insert your actual information:

URL = 'https://{IP_CMS}:{PORT}/api/v1/coSpaces/' where :
  - {IP_CMS} - ip address of your Cisco Meeting Server
  - {PORT} - TCP port

headers = {
  'Authorization': 'Basic {Get Password from Postman app}'
}
  - {Get Password from Postman app} copy authorization code from Postman app
  
  You can use for:
  
  put_passcode_cospace.py - changing password in your CoSpace
  
  get_cospace_setting.py - show detailed settings for your cospace

## Requirements:
 - python 3
 - pip
 - requests
 - xmltodict

## Installation:
	pip install requests
 	pip install xmltodict
## Examples:
python put_passcode_cospace.py

