from calendar import weekday
import smtplib
from decouple import config
import datetime as dt
import random

# The decouple library is used to import the sensitive environment variables from a separate file, 
# and this path is include in the ones to ignore on .gitignore file on the repo
my_email = config("EMAIL")
my_password = config("PASSWORD")
to_mail = config("TO_MAIL")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP(config("SMTP")) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Monday Motivation\n\n {quote}"
            )
