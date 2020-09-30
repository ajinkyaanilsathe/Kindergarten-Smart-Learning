import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secretpw import pw

def main(recv):
	print("inside is ",recv)
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "<your email id here>"
	receiver_email = recv
	password = pw

	message = MIMEMultipart("alternative")
	message["Subject"] = "Kindergarten Smart Learning"
	message["To"] = receiver_email
	
	html = """\
			<html>
			  <body>
			  	<h2>Hi User,</h2>
			  	<p>
			  		<h3>Thank You for Registering with Kindergarten Smart Learning<br><br></h3>

					As each of us navigates the impact of COVID-19 on our lives.
					Know that you are not alone and we are here to help in any way that we can.<Br><Br>

					To educate the very young generation here is free License key to access our Smart Learning Software.

			  	</p><br>
			  	<i> Licene Key </i> - <b>FREEUSER</b>
			  </body>
			</html>
			"""

	# Turn these into plain/html MIMEText objects
	#part1 = MIMEText(text, "plain")
	part1 = MIMEText(html, "html")
	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	#message.attach(part2)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
		    server.ehlo()  # Can be omitted
		    server.starttls(context=context)
		    server.ehlo()  # Can be omitted
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message.as_string())
		    print("Email Sent to ",receiver_email)
		    server.quit()
	except Exception as e:
	    # Print any error messages to stdout
	    print(e)
