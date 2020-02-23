import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 
mailid="icrdet19@gmail.com"
# Authentication 
s.login(mailid, "<password>") 

# message to be sent 
message = "hello message from zimrogroup"

# sending the mail 
s.sendmail("icrdet19@gmail.com", "<to mail address>", message) 

# terminating the session 
s.quit() 
