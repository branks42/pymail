import smtplib

#This program is only designed to run with a gmail account at the moment.
host = 'smtp.gmail.com'
port = 587
username = 'Your email address'
password = 'Your password'

from_email = username
to_list = ['your destination email addresses']

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Your message here")
email_conn.quit()
