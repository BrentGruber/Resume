import os
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template import Context, Template, RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.core.mail import send_mail, EmailMessage
from bio.forms import ContactForm


# Create your views here.
def about(request):
    return render(request, 'bio/about.html')

#View to download pdf using button
def download_resume(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'bio/Brent Gruber Resume 2018.pdf')
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound('The requested pdf was not found in our server.')


#View to send an email from the contact form
def contact(request):
    print("In contact view")
    form_class = ContactForm

    #TODO: this needs to be a try catch in case something isn't there
    #Also should make sure that data is in correct format and prevent header injection
    contact_name = request.POST.get('Name', '')
    contact_email = request.POST.get('Email', '')
    contact_subject = request.POST.get('Subject', '')
    contact_message = request.POST.get('Message', '')

    context = {'contact_name': contact_name,
               'contact_email': contact_email,
               'contact_subject': contact_subject,
               'contact_message': contact_message }
    content = render_to_string('bio/contact_template.txt', context)

    msg = EmailMessage(contact_subject, content, settings.EMAIL_HOST_USER, [settings.DEFAULT_TO_EMAIL])
    msg.send()

    print(msg)

    return redirect('/')