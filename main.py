import smtplib
import datetime as dt
import random


my_email = input("Enter your mail id ->")
password = input("Enter your password ->")
other_person_mail = input("Enter your friends mail id->")

choice = int(input("if your mail is \noutlook ->press 1\nhotmail ->press 2\nyahoo ->press 3\ngmail ->press 4\nPress ->"))
service_provider = ""
if choice == 1:
    service_provider = "smtp-mail.outlook.com"
elif choice == 2:
    service_provider = "smtp.live.com"
elif choice == 3:
    service_provider = "smtp.mail.yahoo.com"
elif choice == 4:
    service_provider = "smtp.gmail.com"


now = dt.datetime.now()  # current day/date/year/time
weekday = now.weekday()  # monday -0 , sunday-6

if weekday == 0:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


with smtplib.SMTP(service_provider) as connection:

    connection.starttls()          # for making connection secure
    connection.login(user=my_email, password=password)     # login my detail
    connection.sendmail(
        from_addr=my_email,
        to_addrs=other_person_mail,
        msg=f"Subject:Motivation for you\n\n{quote}".encode("utf-8"))