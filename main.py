import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(to_email, subject, body, attachment_path, sender_email, sender_password):
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Add the body
        message.attach(MIMEText(body, 'plain'))

        # Add the attachment
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={attachment_path.split("/")[-1]}'
            )
            message.attach(part)

        # Connect to the server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Sender details
sender_email = "mishratanu2222@gmail.com"
sender_password = "hlke lwmo gfhq rjzu"

# Email details
recipients = ["akshatmishra2222@gmail.com", "ashishmpi00012@gmail.com"]
subject = "Job Application"
body = "Hello gandun Please find my resume attached."
attachment_path = "C:/Users/aksha/Downloads/AkshatMishra_SSE_latest.pdf"

# Send emails to each recipient
for recipient in recipients:
    send_email(recipient, subject, body, attachment_path, sender_email, sender_password)
