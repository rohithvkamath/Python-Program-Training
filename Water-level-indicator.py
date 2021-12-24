from time import sleep
def send_mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''
    #The mail addresses and password
    sender_address = 'kamathpratham2001@gmail.com'
    sender_pass = 'xxxx'
    receiver_address = 'rohithkamath2001@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

level = int(input())
if level == 0:
    print("Tank is Empty now")
for i in range (level,100+1,1):
    '''if i==80:
        send_mail()'''
    if i==100:
        print("Tank Full")
        break
    print("Status of tank:",i,"%")
    sleep(1)
    import os
    clear = lambda: os.system('cls')
    clear()