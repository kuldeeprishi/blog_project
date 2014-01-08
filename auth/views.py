from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import RegistrationForm
#from auapp.forms import LoginForm,ChangePass
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required


def registration_view(request):
        form=RegistrationForm()
        if request.method=="POST":
		form = RegistrationForm(request.POST)
                if form.is_valid():
                        name=form.cleaned_data['username']
                        email=form.cleaned_data['email']
                        password=form.cleaned_data['password']
                        cpassword=form.cleaned_data['cpassword']
                        firstname=form.cleaned_data['first_name']
                        lastname=form.cleaned_data['last_name']
                        user=User.objects.create_user(username=name,email=email,password=password)
                        user.first_name = firstname
			user.lastname = lastname
                        return HttpResponse("from has been submit")
                else:
                        return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))
        else:
                 return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))

