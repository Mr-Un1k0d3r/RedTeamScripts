# RedTeamScripts
Repository with various Red Team scripts.

# kill.exe

Performing all kind of activities during a red team and you have several process running that you don't want to close manually. kill.exe is for you. copy it in `C:\Windows\` 
and simply call it with the process name you want to kill.

```
>kill mspaint
killing mspaint 16524
killing mspaint 5284
killing mspaint 8568
killing mspaint 32244
killing mspaint 18908
killing mspaint 12600
killing mspaint 37444
killing mspaint 20492
killing mspaint 36092
killing mspaint 3908
killing mspaint 30980
killing mspaint 37252
killing mspaint 27576
```

# SendGrid SPF bypass

Client that use sendgrid to send email need to add 167.89.0.0/17 to their SPF record to allow sendgrid to send email on their behalf. This is introducing a design flaw that can be leveraged to bypass SPF.

How to:
* Register an account on sendgrid
* Get your API key
* Send email on behalf of your target

Why it's working? sendgrid subnet is part of your target SPF which mean that sedngrid is trusted to send emails on their behalf. Since your account is using sendgrid servers you are part of the whitelist too :)

Which mean that from a Red Team perspective you can send email to your target claiming to be from their own mail domain or send email on their behalf to another organization.

This is a great way to add credibility to your phishing campaign since you can spoof their domain.

#### Is your target vulnerable 

Simply take a look at their DNS TXT record and search for the following subnet 167.89.0.0/17. If it's present you are all set

#### Usage

```
Usage: sendgrid-spf-bypass.py apikey source destination subject emailfile

python sendgrid-spf-bypass.py apikey ceo@target.corp victim@target.corp "Legitimate email" my-email.txt
```

The `emailfile` parameter should be the path to a text file that contain your email. For now the tool only support text message I will improve it in the future.

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

# CFMX6Decryptor

Some people still live in the past. In 2018 we still find ColdFusion MX 6 publicly exposed. This script may help someone retrieving the plain text version of the password that can be extract through the well known path traversal that was affecting ColdFusion.

```
$ java -jar CFMX6Decryptor.jar
ColdFusion MX6 Password decryptor.
Author Mr.Un1k0d3r & Psychan RingZer0 Team 2014

Usage: DecryptCFPassword [uuencoded password]
```

# Credit
Mr.Un1k0d3r RingZer0 Team
