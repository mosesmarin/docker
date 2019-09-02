# Author: Moses
# Date: September 2019
# Description: create qr code and send by e-mail


import qrcode
import time
import os
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def lambda_handler(event, context):
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )
    
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    host = os.environ['SMTPHOST']
    port = os.environ['SMTPPORT']
    mail_from = os.environ['MAIL_FROM']
    mail_to = os.environ['MAIL_TO']    
    mail_sender = os.environ['MAIL_SENDER']    
    mail_receiver = os.environ['MAIL_RECEIVER']
    mail_subject = os.environ['MAIL_SUBJECT']
    mail_body_text = os.environ['MAIL_BODY_TEXT']
    mail_body_html = os.environ['MAIL_BODY_HTML']
    
    
    # Get time in US PACIFIC
    cur=time.time()
    os.environ["TZ"]="US/Pacific"
    time.tzset()
    
    data = "Date is " + time.strftime('%l:%M%p on %b %d, %Y',time.localtime(cur))
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image()
    
    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("/tmp/image.jpg")
    
    message = MIMEMultipart("alternative")
    message["Subject"] = mail_subject
    message["From"] = mail_from
    message["To"] = mail_to
    sender_email = mail_sender
    receiver_email = mail_receiver
    
    # Create the plain-text and HTML version of your message
    text = mail_body_text
    html = mail_body_html
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    # This example assumes the image is in the current directory
    fp = open('/tmp/image.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    
    
    # Send e-mail
    
    server = smtplib.SMTP_SSL(host, port)
    server.login(username, password)
    server.sendmail(
      sender_email, receiver_email, message.as_string()
      )
    server.quit()
    
    return data
