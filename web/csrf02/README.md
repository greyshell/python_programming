# Description

## Bypass double cookie submission CSRF protection
- pattern used: csrf token submission through custom header and cookie
- pre-condition for the exploit
    - victim to use firefox browser with relaxed content blocking policy, chrome is safe
    - assume the app runs in a domain = black.com, there should exist a subdomain like red.black.com
    - attacker has control over the sub-domain like it has the XSS (csrf token cookie of the parent domain can be fix
    via this.)
    - the app has insecure CORS setting 
    ```
    # browser will not set cookie even if this header is set * and Access-Control-Allow-Credentials is set "true"
    # Header set Access-Control-Allow-Origin "*"  
    Header set Access-Control-Allow-Origin "http://localhost:4444"
    
    # allow if you want to expose credentials such as cookies, TLS certificates, authorization.
    Header always set Access-Control-Allow-Credentials "true"
    
    Header add Access-Control-Allow-Methods "GET, POST, PUT, DELETE"
    Header always set Access-Control-Allow-Headers "X-Custom-Header, csrf-token"
    
    # wildcard still doesn’t expose Authorization header, and if you need one, you need to mention explicitly.
    Header always set Access-Control-Expose-Headers "Authorization, *"
    
    # data from Access-Control-Allow-Headers and Access-Control-Allow-Methods headers can be cached for up to 24 hours in Firefox, 2 hours in Chrome (76+).
    # to disable the caching, you can keep the value as -1
    Header always set Access-Control-Max-Age "900"
    ```
- cookie fix via subdomain creates another cookie. it does not modify the existing cookie.
- so when the request gets initiated from the victim's browser then it contains two cookies of same name.
- now which cookie applicaiton will check and process?