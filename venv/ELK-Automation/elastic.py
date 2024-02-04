import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from json import loads

response = requests.get("http://192.168.29.133:9200/_cluster/health?pretty")
response_json = json.loads(response.text)
cluster_name = response_json['cluster_name']
status = response_json['status']
timed_out = response_json['timed_out']
number_of_nodes = response_json['number_of_nodes']
number_of_data_nodes = response_json['number_of_data_nodes']
active_primary_shards = response_json['active_primary_shards']
active_shards = response_json['active_shards']

output = ("Hi Team" + "\n" + "\n" + "\n" + "Please find the Elasticsearch Health Status below:" + "\n" + "cluster_name" + ":" + cluster_name + "\n" + "status" + ":" + status + "\n" + "timed_out" + ":" + str(timed_out) + "\n" + "number_of_nodes" + ":" + str(number_of_nodes) + "\n" + "number_of_data_nodes" + ":" + str(number_of_data_nodes) + "\n" + "active_primary_shards" + ":" + str(active_primary_shards) + "\n" + "active_shards" + ":" + str(active_shards) + "\n" + "\n" + "\n" + "Thanks" + "\n" + "\n" + "Regards" + "\n" + "Automation Team")
print(output)

sender_email = "sachinjobs85@gmail.com"
recipient_email = "ksachin452@gmail.com"
subject = "Elasticsearch Health Status"
attachment_path = "report.txt"
# smtp_server = "smtp.office365.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "sachinjobs85@gmail.com"
smtp_password = "hapr nufu zyon fsls"

# Read the vulnerability report from the file

with open(attachment_path, "rb") as attachment_file:
    attachment_content = attachment_file.read()

# Compose the email

msg = MIMEMultipart('alternative')
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
text = output
# html = """\
# <html>
#   <head></head>
#   <body>
#     <p>'cluster_name'<br>
#        How are you?<br>
#        Here is the <a href="http://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
#part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
#msg.attach(part2)

# Attach the vulnerability report

attachment = MIMEApplication(attachment_content, Name="report.txt")
attachment["Content-Disposition"] = f'attachment; filename="report.txt"'
msg.attach(attachment)

# Connect to the SMTP server and send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(sender_email, recipient_email, msg.as_string())
server.quit()
print("Email Sent with Body")


# S55044466
# Qazxc@1245!