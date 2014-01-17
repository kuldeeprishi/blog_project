# Create your views here.
from contact_us.form import ContactUsForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def v_add_contact(req):
    form=ContactUsForm()
    
    return render_to_response('new_contact.html',{'contact_form':form},context_instance=RequestContext(req))
    
        