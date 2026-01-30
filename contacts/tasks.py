from background_task import background
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags 

@background
def send_async_email(email, name):
    subject = 'Enquiry Confirmation - URC'
    from_email = 'pagesam704@gmail.com'

    html_content = render_to_string('emails/enquiry_confirmation.html', {'name': name, 'email': email})
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()