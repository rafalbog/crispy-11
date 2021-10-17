import smtplib

user = open("user").read()
pwd = open("pwd").read()
FROM = "rafalb"
print(pwd)
TO = open("TO").read()
message = '\n\n\nNever gonna give you up\n\n\n'
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
except:
    print("smt went teerribly wrong, possibly with gmail not accepting 3rd party aps")
