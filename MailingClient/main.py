#we are going to send a mail form an existing mail to a new mail

import smtplib # Import smtplib for the actual sending function for the email
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.outlook.com', 25) # server , port    / server is the smtp server of the mail you are using

server.ehlo() # this is the command that starts the process of sending the mail

with open ('password.txt','r') as f:
    password = f.read()

server.login('anymail@outlook.com', password) # login to the mail

msg = MIMEMultipart()
msg['From'] = 'A smoll Developer' # the name of the sender
msg['To'] = 'secondanymail@outlook.com'
msg['Subject'] = 'Just a test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain')) # attach the message to the mail

filename="funnyImage.jpg"
attachment = open(filename, 'rb') # open the file in read binary mode becasue its image data

p = MIMEBase('application', 'octet-stream') #processing the image data
p.set_payload(attachment.read()) # set the payload of the image data

encoders.encode_base64(p) # encode the image data

p.add_header('Content-Disposition', f'attachment; filename={filename}') # add the header to the image data
msg.attach(p) # attach the image data to the mail

text= msg.as_string() # convert the mail to a string

server.sendmail('anymail@outlook.com', 'secondanymail@outlook.com', text) # send the mail


