import requests
import json

jira_user = 'atlassian_svc_account@podium.io'
jira_password = 'ATATT3xFfGF0hU1V9awvHQh5NtzxrPmwpN8MTPaMoNHKVIF_7gH4o9DkEyJfAIlXY3v9qm5Jt1QBJ7dgrji5Eur2BvXt5lKOD_9AAWQ6lT7kij_q7ns8to0hwMQI8UNYf-27nBVzc6y7WNVxSZlxbb7Toijfi0Nzh-UP54APi6foxJdyPnYT2dA=7940141E'
jira_url = 'https://lendleasegroup.atlassian.net/rest/api/3/search'

headers = {
    "Accept": "application/json",
    "Content": "application/json"
}

query_DCE = {
    'jql': 'project = DCE'
}
#query_IC = {
#    'jql': 'project = IC'
#}

repsonse_DCE = requests.get(jira_url, headers=headers, params=query_DCE, auth=(jira_user, jira_password), verify=False)
#repsonse_IC = requests.get(jira_url, headers=headers, params=query_IC, auth=(jira_user, jira_password), verify=False)

data_DCE = repsonse_DCE.json()
issues_DCE = data_DCE["issues"]

#data_IC = repsonse_IC.json()
#issues_IC = data_IC["issues"]

for issue_DCE in issues_DCE:
    print(json.dumps(issue_DCE))

#for issue_IC in issues_IC:
#    print(json.dumps(issue_IC["key"]))
