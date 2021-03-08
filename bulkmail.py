import csv, smtplib, ssl

sent_from = gmail_user
to = ['{recipient}']
subject = 'enter subj here'
body = '''Dear {name},
...enter content here...
Best Regards,
'''

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

# If using Gmail, turn on "Less secure app access"
from_address = "<enter the email you use to send emails from>"
password = input("Type your password and press enter: ")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(from_address, password)
    with open("./name_mail_real.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row (column titles of name and email)
        for name, email in reader:
            server.sendmail(
                from_address,
                email,
                email_text.format(name=name, recipient=email)
            )
            print('Email sent to:', name, email)
