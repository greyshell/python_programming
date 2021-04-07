#!/usr/bin/env python3

# author: greyshell
# description: use openvpn to access offensive security labs


import argparse
import json
import subprocess
import sys
import time

import keyring
import pexpect
import requests
from colorama import Fore

# global constant variable
PROGRAM_LOGO = """
 _      ____  _____    __  _______  __  _ 
| |__  / () \ | () )   \ \/ /| ()_)|  \| |
|____|/__/\__\|_()_)    \__/ |_|   |_|\__|
"""


class MyUtils:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                description="automate the openvpn lab connection")
        self.parser.add_argument("-c", "--config", metavar="", help="provide a .json file", required=True)


class LoginVpn:
    def __init__(self):
        self._email_to = ""
        self._email_from = ""
        self._email_password = ""
        self._lab_name = ""
        self._lab_user = ""

        self._vpn_user = ""
        self._vpn_password = ""
        self._vpn_config = ""
        self._vpn_command = ""

        self._dns = ""
        self._slack_webhook_url = ""

    def get_parameters(self, config_dict):
        """
        retrieve the value from the input
        :param config_dict: dict
        :return: None
        """
        email_keyring_name = config_dict["email_keyring_name"]
        self._email_to = config_dict["email_to"]
        self._email_from = keyring.get_password(email_keyring_name, 'username')
        self._email_password = keyring.get_password(email_keyring_name, 'password')
        self._lab_name = config_dict["lab_name"]
        self._lab_user = config_dict["lab_user"]

        vpn_keyring_name = config_dict["vpn_keyring_name"]
        self._vpn_user = keyring.get_password(vpn_keyring_name, 'username')
        self._vpn_password = keyring.get_password(vpn_keyring_name, 'password')
        self._vpn_config = config_dict["ovpn_file_path"]

        self._vpn_command = "openvpn" + " " + self._vpn_config

        self._dns = config_dict["dns"]
        self._slack_webhook_url = config_dict["slack_webhook_url"]

        # validate the required input
        if not self._vpn_user and self._vpn_password and self._vpn_config:
            print(f"[x] ovpn_file_path / vpn user credential must be valid")
            sys.exit(0)

    def lab_connection(self):
        """
        connect to the vpn
        :return: None
        """
        try:
            if self._dns:
                print(Fore.GREEN, f"[+] set the dns entry {self._dns} into /etc/resolve.conf")
                set_dns_command = "sed -i \'1s/^/nameserver " + self._dns + "\\n/\' /etc/resolv.conf"
                subprocess.check_output(set_dns_command, shell=True)

            if self._lab_name and self._lab_user and self._email_to and self._email_from and self._email_password:
                send_email_command = "sendEmail -f " + self._email_from + " -t " + self._email_to + \
                                     " -u " + self._lab_name + "-bot: " + self._lab_user + " has logged-in" + \
                                     " -m \'try harder\'" + \
                                     " -s smtp.gmail.com:587 -o tls=yes -xu " + self._email_from + \
                                     " -xp " + self._email_password
                print(Fore.LIGHTMAGENTA_EX, f"[+] sent email notification to {self._email_to}")
                subprocess.check_output(send_email_command, shell=True)

            if self._slack_webhook_url and self._lab_name and self._lab_user:
                bot = self._lab_name + "-bot"
                data = {
                    'text': f':ballot_box_with_check: `{self._lab_user}` has *logged-in* '
                            f':man-lifting-weights:',
                    'username': bot,
                }

                response = requests.post(self._slack_webhook_url, data=json.dumps(data),
                                         headers={'Content-Type': 'application/json'})
                if str(response.text) == 'ok' and str(response.status_code) == '200':
                    print(Fore.LIGHTYELLOW_EX, f"[*] sending slack notification !!")

            print(Fore.WHITE, f"[*] connected to the lab, press ctrl+c to disconnect from the lab")

            # connect to the lab
            i = pexpect.spawn(self._vpn_command)
            i.expect_exact("Enter")
            i.sendline(self._vpn_user)
            i.expect_exact("Password")
            i.sendline(self._vpn_password)

            # delay for 1 day
            time.sleep(3600 * 24)

        except KeyboardInterrupt:
            print(Fore.RED, f"[*] received ctrl+c, disconnecting from lab ")

            if self._lab_name and self._lab_user and self._email_to and self._email_from and self._email_password:
                send_email_command = "sendEmail -f " + self._email_from + " -t " + self._email_to + \
                                     " -u " + self._lab_name + "-bot: " + self._lab_user + " has logged-out" + \
                                     " -m \'sleep tight\'" + \
                                     " -s smtp.gmail.com:587 -o tls=yes -xu " + self._email_from + \
                                     " -xp " + self._email_password

                subprocess.check_output(send_email_command, shell=True)
                print(Fore.GREEN, f"[+] sent email notification to {self._email_to}")

            if self._slack_webhook_url and self._lab_name and self._lab_user:
                bot = self._lab_name + "-bot"
                data = {
                    'text': f':negative_squared_cross_mark: `{self._lab_user}` has *logged-out* '
                            f':tired_face:',
                    'username': bot,
                }

                response = requests.post(self._slack_webhook_url, data=json.dumps(data),
                                         headers={'Content-Type': 'application/json'})
                if str(response.text) == 'ok' and str(response.status_code) == '200':
                    print(Fore.BLUE, f"[*] sending slack notification !!")

            if self._dns:
                print(Fore.GREEN, f"[+] unset the dns entry ")
                unset_dns_command = "sed -i '1d' /etc/resolv.conf"
                subprocess.check_output(unset_dns_command, shell=True)

        except Exception as e:
            print(Fore.MAGENTA, f"[x] error occurs while connecting vpn !")
            print(e)


if __name__ == "__main__":
    my_input = MyUtils()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(0)

    if args.config:
        with open(args.config) as f:
            json_config = json.load(f)

        # display program logo
        print(Fore.GREEN, f"{PROGRAM_LOGO}")

        conn = LoginVpn()
        conn.get_parameters(json_config)
        conn.lab_connection()

    else:
        my_input.parser.print_help(sys.stderr)
