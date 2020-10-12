## Description
`lab_vpn.py` helps to automate the openvpn connection for the InfoSec labs (i.e. PWK / CTP / WAPTx / AWAE).

note:
- you can use `creds_manager.py` helper script to store your vpn and email password in linux keyring.

### Usage
```
usage: lab_vpn.py [-h] -p  -c  -e  -t  [-d]

automate the openvpn lab connection

optional arguments:
  -h, --help      show this help message and exit
  -c , --config   provide a .json file

example:
python lab_vpn.py -c asinha.json

# set email creds into the keyring
keyring set email username
- provide the email_id
keyring set email email_id
- provide the password

# set offsec vpn creds into the keyring
keyring set offsec username
- provide the userid
keyring set offsec user_id
- provide the password
```


 


