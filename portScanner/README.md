## Description
A multi-threaded scanner and enumerator. It quickly finds out all TCP open ports through asynchronous-stateless-scanner `unicornscan` then feeds its result to `nmap` for service fingerprinting. Finally based on the identified services and open ports, it extracts other juicy information.

#### Usage
```
A TCP scanner written in python. During scanning, it uses `nmap`'s top 1000 TCP ports.
```

