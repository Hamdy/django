# Django Tutorial

## Security 

- **General Security settings**

```
# @@@@ Security Settings @@@@ #

# Cookies only sent via https
SESSION_COOKIE_SECURE = True

# CSRF cookie only sent via https
CSRF_COOKIE_SECURE = True

# client-side JavaScript will not be able to access the session cookie.
SESSION_COOKIE_HTTPONLY = True

# prevent visitors from connecting non securely (on production)
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 31536000 # for non frequent users they can not connect non securely even after a year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

- **Install necessary security packages**
```
pip install django-admin-honeypot django-cors-headers django-encrypted-model-fields 
```

**cors**
cors is about a midleware to set `Access-Control-Allow-Origin=`
and `Access-Control-Allow-Headers=`
it is supposed to work in browsers and skips working if 'origin' header is not set

```
INSTALLED_APPS -> ('corsheaders')

Add Middleware 'corsheaders.middleware.CorsMiddleware', before 'corsheaders.middleware.CorsMiddleware'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# CORS_ALLOW_HEADERS has default value (default non standard headers so no need to set unless u know what you are doing)
```


