from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

class Email:
    def __init__(self, user, url):
        self.to = user["correo"]
        self.firstName = user["nombre"].split(" ")[0]
        self.url = url
        self.fromEmail = f"E-ntrenate <{settings.EMAIL_HOST_USER}>"
        # print(user)

    def send_email(self, title, message):
        context = {"mail": self.to, "message": message}
        template = get_template("correo.html")
        content = template.render(context)
        
        email = EmailMultiAlternatives(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [self.to],        
        )
        email.attach_alternative(content, 'text/html')
        email.send()