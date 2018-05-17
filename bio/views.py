import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def about(request):
    return render(request, 'bio/about.html')

def download_resume(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'bio/Brent Gruber Resume 2018.pdf')
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound('The requested pdf was not found in our server.')