## Description
`lab-vpn.py` helps to automate the openvpn connection for the InfoSec labs (i.e. PWK / CTP / WAPTx / AWAE).

note: store your vpn and email password inside linux keyring.

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
keyring set offsec_asinha username
- provide the offsecID
keyring set offsec_asinha offsecID
- provide the password
```


 


