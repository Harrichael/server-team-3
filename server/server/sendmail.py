"""
Sends a verificiation email
"""

def send_email(send_to, code):
	import smtplib
	gmail_user = '' #add email address
	pwd = '' #add password
	FROM = gmail_user
	TO = send_to
	SUBJECT = 'Email Verification'
	TEXT = 'Verificatoin code: %s' %(code)
	
	message = """From: %s\nTo: %s\nSubject: %s\n\n %s""" % (FROM, TO, SUBJECT, TEXT)
	
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print('successfully sent the mail')
	except:
		print("failed to send mail")
	


