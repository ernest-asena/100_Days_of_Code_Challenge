# import smtplib
# import config
import datetime as dt

#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=config.my_email, password=config.password)
#     connection.sendmail(from_addr=config.my_email, to_addrs='ernest.asena@yahoo.com', msg='Subject:Hello\n\nThis is '
#                                                                                           'a Flask URL Paths and the Flask Debugger.py Greeting')

now = dt.datetime.now()
year = now.year
print(now.date())

date_of_birth = dt.datetime(year=1994, month=11, day=1)
print(date_of_birth)