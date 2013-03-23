<pre>

To get this to work in your enivironment:
- in settings.py, update BASE_PATH and database settings

Here's what I added to my apache httpd.conf:

# config for prepay django app
WSGIScriptAlias /prepay /Users/mike/emory/cs370/prepay/prepay/wsgi.py
<Directory "/Users/mike/emory/cs370/prepay">
    AllowOverride None
    Options None
    Order allow,deny
    Allow from all
</Directory>
Alias /prepay/css /Users/mike/emory/cs370/prepay/static/css
Alias /prepay/js /Users/mike/emory/cs370/prepay/static/js
Alias /prepay/img /Users/mike/emory/cs370/prepay/static/img


</pre>