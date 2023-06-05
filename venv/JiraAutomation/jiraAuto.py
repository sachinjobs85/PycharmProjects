from jira import JIRA

# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://splunkjira.atlassian.net"}

# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options=jiraOptions, basic_auth=(
    "sk5131702@gmail.com",
    "ATATT3xFfGF0Sms7gX6e1U8Qf06J5BhTieJ6n2zFEDIWutq7ECY6e--s0dpv5hssyXCgCQkhsgIuhZcjIuHskLUj21xv24GzMmM1j1x65KjhLuIbQnm0PwNQBw31DXtsDvhl2bOJhKI2gvOERTcSeu4nLMppImdLzyx_pYHRj7MxQf-p_VUcEOg=02B566A7"))

# Search all issues mentioned against a project name.
for singleIssue in jira.search_issues(jql_str='project = SPLUN'):
    list = singleIssue.fields.customfield_10020[0]
    #list.sort()
    print(str(list))
    #print('{}, {}, {}, {}, {}, {}'.format(singleIssue.key, singleIssue.fields.issuetype.name, singleIssue.fields.project.key, singleIssue.fields.customfield_10031, singleIssue.fields.customfield_10020[0].name, singleIssue.fields.customfield_10020[0].state, singleIssue.fields.summary,singleIssue.fields.reporter.displayName))
