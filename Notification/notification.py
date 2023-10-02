from twilio.rest import Client
import sys
sys.path.append('.')
from Database.Database import Database

def main(data = []):
    for data in data:
        name, body, phonenumber = data['name'], data['dishes'], data['phonenumber']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_= twilio_phone,
            body=f'Hello {name}, for today\'s menu, you should avoid {body}. Stay healthy!',
            to=phonenumber
            )
        print(message.sid)
        print('message sent succesfully')
        return 0

if __name__ == '__main__':
    sys.exit(main(data = Database()._get_notification_data()))
    
