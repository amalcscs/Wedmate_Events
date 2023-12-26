from django.shortcuts import render,redirect
from wedmateapp.models import *
import os
from django.http import HttpResponse
from datetime import datetime,date, timedelta
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
import qrcode
from django.core.files import File

def base(request):
    return render(request,'base.html')

def wedmate_quotationpdf(request):
    
    
    template_path = 'wedmate_quotation.html'
    context = {
    'media_url':settings.MEDIA_URL,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="letter.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def wedmate_quotationadd(request):
    return render(request,'wedmate_quotation_add.html')