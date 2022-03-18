import smtplib


def automatic_mail():
    user = input("Enter you name: ")
    email = input("Enter your mail: ")
    message = f"""\
Subject: Hi {user},

This is Gohulriya! Hope everyone is fine."""
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # I hid my app passord using * for my security purpose. In your case,
    # you need to enter 16 digit app password. If you did it correctly, It worked.
    s.login("gohulprojects@gmail.com", "*s*e kzcs vecn *anb")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")


automatic_mail()
