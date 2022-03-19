import datetime as dt
import smtplib
import random
import config
#
day_of_the_week = dt.datetime.now().weekday()
print(day_of_the_week)

with open('quotes.txt') as quotes:
    quote = quotes.readlines()
    quote_send = random.choice(quote)
    print(quote_send)
#
if day_of_the_week == 5:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=config.my_email, password=config.password)
        connection.sendmail(from_addr=config.my_email, to_addrs='ernest.asena@yahoo.com',
                            msg=F"Subject:Today's Quote\n\n{quote_send}")

