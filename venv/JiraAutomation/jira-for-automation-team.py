import json

import requests

jira_user = 'atlassian_svc_account@podium.io'
jira_password = 'ATATT3xFfGF0DmVA-FjJGw1qXN_gFMG0xM29Zl8B3glEpH93puIfgf1X3DJWCU1DGwk-1M09_LQW1Cr_DVcuiooPkjHN0qRMavyCjV0Si7EYM0i2af3r6ctOB91AvkSwjkcP32KC69qJRlseXfzALN0OZTGK_zZkCGDmb9iLdmIz30mIM8EXWNI=557FC08B'
jira_url = 'https://lendleasegroup.atlassian.net/rest/api/3/search'

headers = {
    "Accept": "application/json",
    "Content": "application/json"
}

#jql = "project in ('ADHOC', 'SPLUN')"
query_DCE = {
    'jql': 'project = AUTO'
}

repsonse = requests.get(jira_url, headers=headers, params=query_DCE, auth=(jira_user, jira_password), verify=False)

data = repsonse.json()
print(data)
issues = data["issues"]
# for issue in issues:
#     print("================================Start===========================")
#     print(json.dumps(issue))
#     print("================================end===========================")
