## Description
`greyEnum.py` is multi-threaded scanner and enumerator. In stage 1, it quickly finds out all TCP open ports through asynchronous-stateless-scanner `unicornscan`. In stage 2, it feeds the result to `nmap` to fingerprint the running services. In stage 3, it enumerate deeper and extracting more information to identify the exploitation entry point.

#### Usage
```sh
A TCP scanner written in python. During scanning, it uses `nmap`'s top 1000 TCP ports.
```
