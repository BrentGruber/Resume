import os
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template import Context, Template, RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.core.mail import send_mail, EmailMessage
from bio.forms import ContactForm
from .models import Profile


# just render the home profile page, gonna make mine default for now
# Probably should add a home page instead of loading directly into profile
def about(request, prof='Brent Gruber'):
    profile = Profile.objects.get(name=prof)
    print(profile.name)
    return render(request, 'bio/about.html', {'profile' : profile})

#View to download pdf using button
def download_resume(request, prof):
    profile = Profile.objects.get(name=prof)
    file_path = profile.resume.path

    #if the file exists then send it as an httpresponse, else notify user it was not found
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound('The requested pdf was not found in our server.')


#View to send an email from the contact form
def contact(request, prof):

    profile = Profile.objects.get(name=prof)

    try:
        #get all the details of the email from the POST library
        contact_name = request.POST.get('Name', '')
        contact_email = request.POST.get('Email', '')
        contact_subject = request.POST.get('Subject', '')
        contact_message = request.POST.get('Message', '')

        #build the context to format the message
        context = {'contact_name': contact_name,
                   'contact_email': contact_email,
                   'contact_subject': contact_subject,
                'contact_message': contact_message }
        content = render_to_string('bio/contact_template.txt', context)

        #send the messge from the default sending account to the default receiving account defined in settings
        msg = EmailMessage(contact_subject, content, settings.EMAIL_HOST_USER, [profile.email])
        msg.send()

        response = "Message sent successfully"
    except e:
        response = "Message failed"

    #For now just redirect to homepage, need to figure out how to notify user message was sent
    return redirect('bio:about', prof=profile.name)