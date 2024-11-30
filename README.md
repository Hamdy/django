# Django Tutorial

- [Add Vscode](https://github.com/Hamdy/django/commit/3a838ebe082307c3e28215582aa410069af64bb1)
- [Add Requirements](https://github.com/Hamdy/django/commit/b2a9ec77e683ebc68122c435384a28c33ecbe11d)
- [Add Environment Variables support](https://github.com/Hamdy/django/commit/091f39c84fcd7f5286e0e4ba4de992b8dadc339a)
- [Add Security Settings](https://github.com/Hamdy/django/commit/fbe94de963228a3082bc821546afb65563ced7fb)
- [Add Models and model admin examples](https://github.com/Hamdy/django/commit/6bc4f86f2ffab7d9175e2debf92c9ed200b58535)
- [Custom user, Auth backend, File backend, and a middleware](https://github.com/Hamdy/django/commit/6bc4f86f2ffab7d9175e2debf92c9ed200b58535)
- [Content Security Policy / CSP](https://github.com/Hamdy/django/commit/53aefe85c39ea5633e885d66a283208e2b905fc0)
- [Add Commands](https://github.com/Hamdy/django/commit/4ea648e75cfa0e542d620930d4e60559c01ded33)


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


