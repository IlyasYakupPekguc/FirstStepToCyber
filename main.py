#we are going to send a mail form an existing mail to a new mail

import smtplib # Import smtplib for the actual sending function for the email

server = smtplib.SMTP('smtp.gmail.com', 25) # server , port    / server is the smtp server of the mail you are using

server.ehlo() # this is the command that starts the process of sending the mail

with open ('password.txt','r') as f:
    password = f.read()

server.login('ilyas.pekgucnl@gmail.com', password) # login to the mail
