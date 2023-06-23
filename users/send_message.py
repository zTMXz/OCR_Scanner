from django.core.mail import send_mail

def send_message(username, password, email, email_host_user):
    send_mail(subject='Successful Registration Message',
              message=f"""
You have successfully registered on DockieScanner
Your login details:
===============================
    username: {username}
    password: {password}
===============================
""",
              recipient_list=[email],
              from_email=email_host_user
              )
