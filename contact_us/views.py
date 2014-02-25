# Create your views here.
from contact_us.form import ContactUsForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import  HttpResponseRedirect
from contact_us.models import ContactUs
from django.core.mail import send_mail
from django.conf import settings

def v_add_contact(req):
    form=ContactUsForm()
    if req.method=="POST":
        form=ContactUsForm(req.POST)
        if form.is_valid():
            ContactUs.objects.create(name=form.cleaned_data['name'],
                                     contact_no=form.cleaned_data['contact_no'],
                                     email=form.cleaned_data['email'],
                                     message=form.cleaned_data['message']
                                     )
            subject = 'Message from - {0}'.format(form.cleaned_data['name'])
            send_mail(subject, form.cleaned_data['message'], 'visitor@moocsmagzine.com', settings.CONTACTUS)
            return HttpResponseRedirect('/')
            
    return render_to_response('new_contact.html',{'contact_form':form},context_instance=RequestContext(req))
