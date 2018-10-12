# RedTeamScripts
Repository with various Red Team scripts.

# Password spraying

Install the following dependencies
```
pip install requests_ntlm
pip install requests
```

```
$ python password-spray.py
PasswordSpraying v1.0

Usage: %s [user list] [domain] [url] [password]

$ python password-spray.py users.txt RINGZER0 https://lyncweb.ringzer0team.com/abs/ Summer2018
```

Note that various end points can be used to validate the user credentials. The subdomain for Lync and on premise OWA may be different. Use the autodiscover feature to retrieve the right url for your target:
* Lync (https://lyncweb.target.com/abs/)
* Office 365 (https://autodiscover-s.outlook.com/autodiscover/autodiscover.xml) (use email instead of DOMAIN\USER format)
* On premise OWA (https://mail.target.com/EWS/Exchange.asmx)
    
There is several other urls that can be used for Lync & On premise OWA.

# Credit
Mr.Un1k0d3r RingZer0 Team
