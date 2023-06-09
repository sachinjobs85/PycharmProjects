import requests
import json
from datetime import datetime
import os

jira_user = 'sk5131702@gmail.com'
jira_password = 'ATATT3xFfGF0Sms7gX6e1U8Qf06J5BhTieJ6n2zFEDIWutq7ECY6e--s0dpv5hssyXCgCQkhsgIuhZcjIuHskLUj21xv24GzMmM1j1x65KjhLuIbQnm0PwNQBw31DXtsDvhl2bOJhKI2gvOERTcSeu4nLMppImdLzyx_pYHRj7MxQf-p_VUcEOg=02B566A7'
jira_url = 'https://splunkjira.atlassian.net/rest/api/3/search'

headers = {
    "Accept": "application/json",
    "Content": "application/json"
}

query = {
    'jql': 'project = SPLUN'
}

repsonse = requests.get(jira_url, headers=headers, params=query, auth=(jira_user, jira_password), verify=False)
# print(repsonse.text)

data = repsonse.json()
issues = data["issues"]
for issue in issues:
    print(issue["fields"]["customfield_10031"])
    print(issue["fields"]["customfield_10020"])
    print("Done")
