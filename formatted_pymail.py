import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = 'smtp.gmail.com'
port = 587
username = 'Your email address'
password = 'Your password'
from_email = username
to_list = ['List of recipient email addresses']

class MessageUser():
	user_details = []
	messages = []
	email_messages = []
	base_message = '''Hello {name}!

Thank you for reaching out on {date}. Just as a 
reminder, the puchase total was ${total}.

Thanks!
'''

	def add_user(self, name, amount, email=None):
		name = name[0].upper() + name[1].lower()
		amount = "%.2f" %(amount)
		detail = {
			'name': name,
			'amount': amount,
		}
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text
		if email is not None:
			detail['email'] = email
		self.user_details.append(detail)

	def get_details(self):
		return self.user_details

	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail['name']
				amount = detail['amount']
				date = detail['date']
				message = self.base_message
				new_msg = message.format(
					name=name,
					date=date
					total=amount
				)
				user_email = detail.get('email')
				if user_email:
					user_data = {
						"email":user_email,
						"message": new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)
			return self.messages
		return []

	def send_email(self):
		#Format the messages
		self.make_messages()
		#Check to make sure it's used
		if len(self.message) > 0:
			#Go through messages
			for detail in self.email_messages:
				#Get details that are in it
				user_email = detail['email']
				user_message = detail['message']
				#run email
				try:
					email_conn = smtplib.SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(username, password)

					the_msg = MIMEMultipart('alternative')
					the_msg['Subject'] = 'Subject line here'
					the_msg['From'] = from_email
					the_msg['To'] = user_email

					part_1 = MIMEText(user_message, 'plain')

					the_msg.attach(part_1)
					the_msg.attach(part_2)

					email_conn.sendmail(from_email, to_list, the_msg.as_string())
					email_conn.quit()
				except smtplib.SMTPException:
					print('Error sending message.')
			return True
		return False

obj = MessageUser()
obj.add_user('name', 143.43, email='email@email.com')
obj.add_user('name', 143.43, email='email@email.com')
obj.add_user('name', 143.43, email='email@email.com')
obj.add_user('name', 143.43, email='email@email.com')
obj.add_user('name', 143.43, email='email@email.com')
obj.get_details()
#send mail
obj.send_email()
