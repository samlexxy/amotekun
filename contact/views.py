from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             message = request.POST.get('message')

#             full_message = f"Message from {name} ({email}):\n\n{message}"
#             # breakpoint()

#             send_mail(
#                 subject="New Contact Form Message",
#                 message=full_message,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[settings.CONTACT_EMAIL],
#             )

#             # Optional: redirect or show success message
#             messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
#             return render(request, 'contact/contact.html', {'success': True})

#     return render(request, 'contact/contact.html')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject="New Contact Form Message",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
            )

            messages.success(request, 'Your message has been sent successfully! Thank you!')
            return render(request, 'contact/contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
