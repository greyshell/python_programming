#!/usr/bin/env python3

# author: greyshell

import requests
import json
import os

if __name__ == '__main__':
    wekbook_url = os.environ['SLACK_WEBHOOK_URL']

    data = {
        'text': '> Test Python',
        'username': 'bot',
    }

    response = requests.post(wekbook_url, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))