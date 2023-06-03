import requests
import json
from datetime import datetime
import os

jira_user = 'sk5131702@gmail.com'
jira_password = 'ATATT3xFfGF0Sms7gX6e1U8Qf06J5BhTieJ6n2zFEDIWutq7ECY6e--s0dpv5hssyXCgCQkhsgIuhZcjIuHskLUj21xv24GzMmM1j1x65KjhLuIbQnm0PwNQBw31DXtsDvhl2bOJhKI2gvOERTcSeu4nLMppImdLzyx_pYHRj7MxQf-p_VUcEOg=02B566A7'
jira_url = 'https://splunkjira.atlassian.net'

time_temp = datetime.now()
time_present = time_temp.strftime('%Y-%m-%d %H:%M')

# time_file = open("script.txt")
# time_last = time_file.read()
# time_file.close()

boards_req = requests.get(jira_url + '/rest/agile/1.0/board', auth=(jira_user, jira_password), verify=False)
if boards_req.status_code == 200:
    boards_data = json.loads(boards_req.content)
    boards = boards_data['values']
    #print(boards)
    for board in boards:
        if board['type'] == 'scrum':
            sprints_req = requests.get(jira_url + '/rest/agile/1.0/board/' + str(board['id']) + '/sprint',
                                       auth=(jira_user, jira_password), verify=False)
            # print(sprints_req)
            if sprints_req.status_code == 200:
                sprints_data = json.loads(sprints_req.content)
                sprints = sprints_data['values']
                # print(sprints)
                for sprint in sprints:
                    issues_req = requests.get(jira_url + "/rest/agile/1.0/board/" + str(board['id']) + "/sprint/" + str(
                        sprint['id']) + "/issue/", auth=(jira_user, jira_password), verify=False)
                    print(issues_req)
                    if issues_req.status_code == 200:
                        issues_data = json.loads(issues_req.content)
                        # print(issues_data)
                        issues = issues_data['issues']
                        # print(issues)
                        data = {}
                        for issue in issues:
                            #print(issue)
                            fields = issue['fields']
                            data['board'] = board
                            data['issue'] = issue
                            data['sprint_name'] = sprint
                            data['updated'] = fields.get('updated', 'None')
                            data['key'] = issue['key']
                            data['status'] = fields.get('status', 'None')
                            data['fields'] = fields.get('fields', 'None')
                            # print(data)
                            #print(json.dumps(data))
                            print(json.dumps(data['board']['name']), end=',')
                            print(json.dumps(data['issue']['fields']['parent']['key']), end=',')
                            print(json.dumps(data['issue']['fields']['parent']['fields']['summary']), end=',')
                            print(json.dumps(data['board']['location']['projectName']), end=',')

                            print(json.dumps(data['sprint_name']['name']), end=',')
                            print(json.dumps(data['sprint_name']['state']), end=',')
                            print(json.dumps(data['sprint_name']['startDate']), end=',')
                            print(json.dumps(data['sprint_name']['endDate']), end=',')
                            print(json.dumps(data['issue']['id']), end=',')
                            print(json.dumps(data['issue']['key']), end=',')
                            print(json.dumps(data['issue']['fields']['summary']), end=',')
                            print(json.dumps(data['issue']['fields']['status']['name']), end=',')
                            #print(json.dumps(data['issue']['fields']['assignee']['displayName']))
                            print(json.dumps(data['issue']['fields']['parent']['priority']['name']))
                            # print(json.dumps(data['issue']['fields']['customfield_10031']), end=',')
                            # print(json.dumps(data['issue']['fields']['creator']['displayName']), end=',')
                            # print(json.dumps(data['issue']['fields']['lastViewed']))
                            # print(json.dumps(data['issue']['fields']['created']), end=',')
                            # print(json.dumps(data['issue']['fields']['status']['name']), end=',')
                            # print(json.dumps(data['issue']['fields']['description']), end=',')
                            # print(json.dumps(data['issue']['fields']['assignee']['active']))
