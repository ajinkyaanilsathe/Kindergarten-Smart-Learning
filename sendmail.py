import smtplib, ssl
from secretpw import pw

def send_mail(receiver_email):
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "trail.abc.xyz@gmail.com"
	receiver_email = "ajinkyaanilsathe@gmail.com" #ajinkyaanilsathe@gmail.com
	password = pw

	message = """From: Kindergarten Smart Learning <from@fromdomain.com>
	MIME-Version: 1.0
	Content-type: text/html
	Subject: Kindergarten Smart Learning

	<i>Thank You for Registering with Kindergarten Smart Learning</i><br>

	<br>As each of us navigates the impact of COVID-19 on our lives.
	Know that you are not alone and we are here to help in any way that we can.

	<br>To educate the very young generation here is free License key to access our Smart Learning Software.

	<br><br>Key - <b>FREEUSER</b>
	"""

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  # Can be omitted
		    server.starttls(context=context)
		    server.ehlo()  # Can be omitted
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
		    print("Email Sent to ",receiver_email)
		    server.quit()
	except Exception as e:
	    # Print any error messages to stdout
	    print(e)