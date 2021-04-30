import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def otp_on_email(email_id):
    fromaddr = "OtPTEst@gmail.com" #tu email
    senders_pass = "something" #contraseña del email
    toaddr = email_id #el que va a recibir el email

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "OTP by Pablo (Encr0)"

    otp = random.randrange(100001, 999999)
    body = '''
    tu otp es [ {} ] y lo puedes usar para verificar tu cuenta.
           ---------------------------------
           Encr0 on github, pablosnaxx on instagram
                    feel free to contact 
    '''.format(otp)
