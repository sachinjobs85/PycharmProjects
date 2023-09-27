import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email configuration

sender_email = "sachinjobs85@gmail.com"
recipient_email = "ksachin452@gmail.com"
subject = "Docker Image Vulnerability Report"
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

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

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
print("Email Sent")
