# Pen-Test

#### greyEnum.py
A multi-threaded scanner and enumerator. It quickly finds out all TCP open ports through asynchronous-stateless-scanner `unicornscan` then feeds its result to `nmap` for service fingerprinting. Finally based on the identified services and open ports, it extracts other juicy information.

#### lightPortScanner.py
A TCP scanner written in python. During scanning, it uses `nmap`'s top 1000 TCP ports.

#### linuxJuicer.sh
During post exploitation, it extracts juicy information to identify possible privilege escalation vectors.

#### winEnum.bat
During post exploitation, it extracts juicy information to identify possible privilege escalation vectors.

#### winEnum_wmc.bat
During post exploitation, it extracts juicy information to identify possible privilege escalation vectors using `wmic`.
