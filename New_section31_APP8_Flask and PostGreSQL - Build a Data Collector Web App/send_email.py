from email.mime.text import MIMEText
import smtplib


def send_email(email_id, height, average_height, count):
    print("Inside else send email")
    print(email_id, height, average_height)
    from_email = 'udit123bhatiya@gmail.com'
    to_email = email_id
    subject = "APP : Average Height Stats"
    message = f"""
    Hi there, 
    <br>
    <br>User <strong> {email_id} </strong> is having height <strong> {height} cm(s). </strong>
    <br>Average height of <strong> {count} </strong> users available  is <strong> {average_height} cm(s). </strong>
    <br>
    <br>Thanks and Regards,
    <br>Automated Code
    """

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    ## USING GMAIL SERVER

    gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
    gmail_server.set_debuglevel(1)
    gmail_server.ehlo()
    gmail_server.starttls()
    gmail_server.login(from_email, '9027720016@')
    gmail_server.send_message(msg)

    # ## USING  DEERE SERVER
    # smtp_server = 'mailhost.dx.deere.com'
    # server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    #
    # server.sendmail(msg['From'], msg["To"].split(";"), msg.as_string())
    # server.quit()


# send_email('udit1234bhatiya@gmail.com', 125, 166)
