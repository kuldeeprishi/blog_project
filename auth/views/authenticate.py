
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.mail import send_mail

# 
# def if_login(f):
#     print "in "
#     def f(request,*args,**kwargs):
#         #print "args=",args
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect("/")
#         else:
#             return f
#     print "out "
#     return f


def v_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
        
    if request.method=="POST":
        errors=[]
        email = request.POST.get('email','').strip()
        password = request.POST.get('password','').strip()
        
        if not email or not password:
            errors.append('Please enter your email and password .')
            
        if not errors:
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    errors.append("Your account is  temporary disabled . ")
            else:
                errors.append("Invalid email Or password . ")
            
    return render_to_response('authenticate/login.html',locals(),context_instance=RequestContext(request))
    

def v_home(request):
    if request.user.is_authenticated():
        return HttpResponse('''this page should be served as home page . <a href="/logout">Logout</a>''')
    else:
        return HttpResponse('''this page should be served as home page . <a href="/login">Login</a>''')
    #if request.user.is_authenticated():


def v_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    

def v_forgotPassword(request):
    if request.method=="POST":
        errors=[]
        email = request.POST.get('email','').strip()
        
        if not email:
            errors.append('Please enter email Id .')
        elif '@' not in email:
            errors.append('Please enter valid email Id .')
        elif not User.objects.filter(email=email):
            errors.append("Email Id is not registered with us .")
        
        if not errors:
            import os
            user=User.objects.get(email=email)
            password=os.urandom(5).encode('hex')
            user.set_password(password) 
            user.save()
            msg='''
            Hi {name},
            
            Your New Password is inside double quotes, "{password}" .
            
            Thanks & Regards,
            Moocs Mentors Team
            '''.format(
                       name=user.username,
                       password=password
                       )
            from threading import Thread
            Thread(target=send_mail,args=['Your new password',msg,'BRENTWOOD',[user.email]]).start()
            return render_to_response('authenticate/forgotPassword.html',{'messages':['Password successfully sent to your email id .']},context_instance=RequestContext(request))
            
    return render_to_response('authenticate/forgotPassword.html',locals(),context_instance=RequestContext(request))


def v_resetPassword(request):
    if request.user.is_authenticated():
        if request.method=="POST":
            errors=[]
            password=request.POST.get('password','').strip()
            cpassword=request.POST.get('cpassword','').strip()
            
            if not password:
                errors.append("please enter new password .")
            elif not cpassword:
                errors.append("please enter confirm password .")
            elif password!=cpassword:
                errors.append("Confirm password not matched .")
            
            if not errors:
                request.user.set_password(password)
                request.user.save()
                return render_to_response('authenticate/resetPassword.html',{'messages':['Password successfully changed .']},context_instance=RequestContext(request))        
                
        return render_to_response('authenticate/resetPassword.html',locals(),context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
    

    
    
    
    
    