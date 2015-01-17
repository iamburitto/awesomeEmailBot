from datetime import datetime, time
# from time import sleep

# Import smtplib for the actual sending function
import smtplib
from email.mime.base import MIMEBase
import mimetypes
import zipfile
from email import encoders

#os
import os

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#time and sleep
import datetime
import time
current_time = datetime.datetime.now().time()
current_time_isoformat = current_time.isoformat()
flag = True

while(flag):
	current_time = datetime.datetime.now().time()
	# current_time_isoformat = current_time.isoformat()
	 # and current_time_isoformat < '10:17:15.0'
	desired_time = current_time.replace(hour=12, minute=4, second=0, microsecond=0)
	if(current_time > desired_time):

		# Open a plain text file for reading.  For this example, assume that
		# the text file contains only ASCII characters.
		fp = open('template.txt', 'rb')
		img_data_1 = open('britt.jpg', 'rb').read()
		img_data_2 = open('evan.jpg', 'rb').read()
		img_data_3 = open('trevor.jpg', 'rb').read()
		img_data_4 = open('kevin.jpg', 'rb').read()
		msg = MIMEMultipart()
		# Create a text/plain message
		text = MIMEText(fp.read())
		msg.attach(text)
		fp.close()

		#add the images
		image = MIMEImage(img_data_1, name=os.path.basename('britt.jpg'))
		msg.attach(image)
		image = MIMEImage(img_data_2, name=os.path.basename('evan.jpg'))
		msg.attach(image)
		image = MIMEImage(img_data_3, name=os.path.basename('kevin.jpg'))
		msg.attach(image)
		image = MIMEImage(img_data_4, name=os.path.basename('trevor.jpg'))
		msg.attach(image)
		

		me = "iamburitto@gmail.com" # the sender's email address

		you = "ckrintz@gmail.com" # the recipient's email address
		msg['Subject'] = '189a project selection'
		msg['From'] = me
		msg['To'] = you

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls() # upgrades plain text to secure
		# log in to the server
		server.login("iamburitto", "@gmil42bkc@")

		# Send the message via our own SMTP server
		server.sendmail(me, [you], msg.as_string())
		server.quit()
		# get current time again
		current_time = datetime.datetime.now().time()
		desired_time = current_time.replace(hour=12, minute=4, second=0, microsecond=0)

		if current_time > desired_time:
			break