## Description
`creds_manager.py` - a wrapper to the linux `keyring` that manages the credential in a secure way.

### Usage
```
usage: creds_manager.py [-h] {set,get,del} ...

a helper script / wrapper to perform all keyring operations

optional arguments:
  -h, --help     show this help message and exit

commands:
  {set,get,del}  See '[command] --help' for details
    set          set up a keyring
    get          get credentials from a keyring
    del          delete a keyring

```

```
usage: creds_manager.py set [-h] -n  -u  -p

set up a keyring

optional arguments:
  -h, --help        show this help message and exit
  -n , --name       provide the keyring name
  -u , --username   provide the username
  -p , --password   provide the password
```

 


