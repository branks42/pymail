from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = 'smtp.gmail.com'
port = 587
username = 'Your email address'
password = 'Your password'
from_email = username
to_list = ['List of recipient email addresses']
try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)

	the_msg = MIMEMultipart('alternative')
	the_msg['Subject'] = 'Subject line here'
	the_msg['From'] = from_email
	#the_msg['To'] = to_list

	plain_txt = 'Test message here'
	html_txt = '''\
	<html>
	  <head></head>
	  <body>
	    <p>Hello.<br>
	      Test <b>message</b>
	    </p>
	  </body>
	</html>
	'''

	part_1 = MIMEText(plain_txt, 'plain')
	part_2 = MIMEText(html_txt, 'html')

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPException:
	print('Error sending message.')