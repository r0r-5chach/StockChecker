import smtplib, ssl
import yagmail

port = 465
context = ssl.create_default_context()


def mail_user(recipient, subject, message):
    yag = yagmail.SMTP("isitstocked", "B0tp@ssword")
    yag.send(to=recipient, subject=subject, contents=message)
