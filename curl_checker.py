'''curl -s -d "YII_CSRF_TOKEN=535ab25961950109832e8df490d1b6d300224460&OrderItem%5BpreferredDate%5D=2019-10-25&OrderItem%5BminDate%5D=2019-10-18&OrderItem%5Bproduct%5D%5Bid%5D=343915&ItemQuantity%5B343915%5D%5B0%5D%5BpriceOption%5D%5Bid%5D=3545586&ItemQuantity%5B343915%5D%5B0%5D%5Bquantity%5D=1&ItemQuantity%5B343915%5D%5B1%5D%5BpriceOption%5D%5Bid%5D=3545587&OrderItem%5BselectedSessionId%5D=134766371&OrderItem%5BsessionId%5D=134766371" -X POST https://lasafaris.rezdy.com/updateTotalprice | python3 -c "import sys, json; print(json.load(sys.stdin)['sessionTimeLabel']['134766374'])"
'''

import datetime
import json
import os
import sys
from twilio.rest import Client

URL = 'https://lasafaris.rezdy.com/343915/malibu-lights'
TWILIO_SID = os.environ.get('TW_PUBLIC')
TOKEN = os.environ.get('TW_SECRET')
PHONE_TO = os.environ.get('PH')
PHONE_FROM = os.environ.get('TW_PH')
MESSAGE = 'The 8pm ticket is available! {}'


def main():
    client = Client(TWILIO_SID, TOKEN)
    json_response = json.load(sys.stdin)
    ticket_info = json_response['sessionTimeLabel']['134766374']
    log(ticket_info)

    # Test
    # ticket_info = '8:00 PM - 1 Available'

    is_available = 'Available' in ticket_info
    if is_available:
        log('Ticket is Available!')
        client.messages.create(to=PHONE_TO,
                               from_=PHONE_FROM,
                               body=MESSAGE.format(URL))
    else:
        log('Ticket is Sold Out!')


def log(s):
    print(datetime.datetime.now(), s)


if __name__ == '__main__':
    main()
