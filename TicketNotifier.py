#!/home/jzaremba/bin/python

import requests
import json
import os
import FDcredentials


# The notifier function
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Sosumi"' 
              """.format(text, title))


# change me
api_key = FDcredentials.api_key
domain = FDcredentials.domain
password = FDcredentials.password

# Take all tickets
r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password))

if r.status_code == 200:
  arrayResponse  = json.loads(r.content)
  # if ticket status is open custom fields are not set - notify
  for response in arrayResponse:
    if(response["status"] == 2 and response["custom_fields"]["cf_code_change_required"]==None):
        notify("New ticket, no. " + str(response["id"]) + " in FD", response["subject"])
else:
  print("Failed to read tickets, errors are displayed below,")
  response = json.loads(r.content)
  print(response["errors"])
  print("x-request-id : " + r.headers['x-request-id'])
  print("Status Code : " + str(r.status_code))