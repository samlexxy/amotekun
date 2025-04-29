from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # contact = form.save()
            # full_message = f"Message from {contact.name} ({contact.email}):\n\n{contact.message}"

            # send_mail(
            #     subject="New Contact Form Message",
            #     message=full_message,
            #     from_email=settings.DEFAULT_FROM_EMAIL,
            #     recipient_list=[settings.CONTACT_EMAIL],
            # )

            messages.success(request, 'Your message has been sent successfully! Thank you!')
            return render(request, 'contact/contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
