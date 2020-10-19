#!/usr/bin/env python3

# author: greyshell

import requests
import json

if __name__ == '__main__':

    wekbook_url = 'https://hooks.slack.com/services/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'

    data = {
        'text': 'logged-In: asinha',
        'username': 'awae-bot',
    }

    response = requests.post(wekbook_url, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))