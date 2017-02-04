## Description
`extractor.py` is multi-threaded scanner and enumerator. In stage 1, it quickly finds out all TCP open ports through asynchronous-stateless-scanner `unicornscan`. In stage 2, it feeds the result to `nmap` to fingerprint the running services. In stage 3, it enumerate deeper and extracting more information to identify the exploitation entry point.

1. Phase 1: Quickly identifies all open TCP & UDP ports through asynchronous-stateless-scanner `unicornscan`.
2. Item 2: Feeds results to `nmap` for fingerprinting the running services.
3. Item 3: Enumerate deeper and extracts more information to determine the vulnerable entry point.

#### Usage
```sh
Usage: python extractor.py -H <target host>

Options:
  -h, --help  show this help message and exit
  -H HOST     specify target host
  -M TARGETS  provide a text file (i.e. targets.txt) to scan multiple hosts
              where each host should be separated by a new line

```
git init && git add . && git status && git commit -m "new structure" && git push -u origin master